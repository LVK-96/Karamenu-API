"""Get menus from Sodexo/Fazer api and create new Menu object."""
import json
from datetime import date
from apps.api.models import Menu
from .course import Course
import apps.menu_parser.sodexo as sodexo
import apps.menu_parser.fazer as fazer
from .serializers import CourseSerializer


def parse_menu(restaurant, d):
    """Create new menu object."""
    if restaurant.company == "Sodexo":
        menu = json.loads(sodexo.get_json(restaurant.api_id, d))
        try:
            courses = sodexo.parse_courses(menu["courses"])
        except TypeError:
            not_available = Course("", "Ei saatavilla", "", "", "", "", "")
            courses = CourseSerializer([not_available], many=True).data
            return Menu.create(restaurant, d, courses)
    elif restaurant.company == "Fazer":
        delta = (d - date.today()).days
        if d < date.today() or delta > 7:
            # Fazer api only has the menus for the current week
            not_available = Course("", "Ei saatavilla", "", "", "", "", "")
            courses = CourseSerializer([not_available], many=True).data
            return Menu.create(restaurant, d, courses)

        menu = json.loads(fazer.get_json(restaurant.api_id))
        try:
            courses = fazer.parse_courses(
                    menu["MenusForDays"][delta]["SetMenus"])
        except IndexError:
            not_available = Course("", "Ei saatavilla", "", "", "", "", "")
            courses = CourseSerializer([not_available], many=True).data
            return Menu.create(restaurant, d, courses)
    else:
        not_available = Course("", "Ei saatavilla", "", "", "", "", "")
        courses = [not_available]

    courses = CourseSerializer(courses, many=True).data
    new_menu = Menu.create(restaurant, d, courses)
    return new_menu
