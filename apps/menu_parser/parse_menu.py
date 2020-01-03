"""Get menus from Sodexo/Fazer api and create new Menu object."""
import json
import requests.exceptions
from datetime import date
from apps.api.models import Menu
from .course import Course
import apps.menu_parser.sodexo as sodexo
import apps.menu_parser.fazer as fazer
from .serializers import CourseSerializer


class CompanyError(Exception):
    """Raise this if company is unknown"""
    pass


def parse_menu(restaurant, d):
    """Create new menu object."""
    try:
        if restaurant.company == "Sodexo":
            menu = json.loads(sodexo.get_json(restaurant.api_id, d))
            courses = sodexo.parse_courses(menu["courses"])
        elif restaurant.company == "Fazer":
            delta = (d - date.today()).days
            menu = json.loads(fazer.get_json(restaurant.api_id))
            courses = fazer.parse_courses(
                    menu["MenusForDays"][delta]["SetMenus"])
        else:
            raise CompanyError
    except (requests.exceptions.HTTPError, TypeError, IndexError, CompanyError):
        not_available = Course("", "Ei saatavilla", "", "", "", "", "")
        courses = [not_available]

    courses = CourseSerializer(courses, many=True).data
    new_menu = Menu.create(restaurant, d, courses)
    return new_menu
