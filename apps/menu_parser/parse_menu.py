"""Get menus from Sodexo/Fazer api and create new Menu object."""
import json
from apps.api.models import Menu
from . import sodexo
from .serializers import CourseSerializer


def parse_menu(restaurant, d):
    """Create new menu object."""
    # TODO: support fazer.
    menu = json.loads(sodexo.get_json(restaurant.id, d))
    courses = sodexo.parse_courses(menu["courses"])
    courses = CourseSerializer(courses, many=True).data
    new_menu = Menu.create(restaurant, d, courses)
    new_menu.save()
    return new_menu
