"""Get menus from Sodexo/Fazer api and create new Menu object."""
import json
from apps.api.models import Menu
from .sodexo import get_json, parse_courses
from .serializers import CourseSerializer


def parse_menu(restaurant, d):
    """Create new menu object."""
    # TODO: support fazer.
    menu = json.loads(get_json(restaurant.id, d))
    try:
        courses = parse_courses(menu["courses"])
        courses = CourseSerializer(courses, many=True).data
        new_menu = Menu.create(restaurant, d, courses)
    except KeyError:
        new_menu = None
    
    return new_menu
