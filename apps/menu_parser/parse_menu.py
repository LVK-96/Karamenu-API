"""Get menus from Sodexo/Fazer api and create new Menu object."""
import json
from datetime import date
from apps.api.models import Menu
import apps.menu_parser.sodexo as sodexo
import apps.menu_parser.fazer as fazer
import apps.menu_parser.api_lookup as api_lookup
from .serializers import CourseSerializer


def parse_menu(restaurant, d):
    """Create new menu object."""
    if restaurant.name in api_lookup.sodexo:
        menu = json.loads(sodexo.get_json(restaurant.name, d))
        try:
            courses = sodexo.parse_courses(menu["courses"])
        except KeyError:
            return Menu.create(restaurant, d, "{}")
    elif restaurant.name in api_lookup.fazer:
        delta = (d - date.today()).days
        if d < date.today() or delta > 7:
            # Fazer api only has the menus for the current week
            return Menu.create(restaurant, d, "{}")
        menu = json.loads(fazer.get_json(restaurant.name))
        try:
            print(delta)
            print(menu["MenusForDays"][delta])
            print(len(menu["MenusForDays"]))
            courses = fazer.parse_courses(
                    menu["MenusForDays"][delta]["SetMenus"])
        except KeyError:
            return Menu.create(restaurant, d, "{}")

    courses = CourseSerializer(courses, many=True).data
    new_menu = Menu.create(restaurant, d, courses)
    return new_menu
