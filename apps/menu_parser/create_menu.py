"""Get menus from Sodexo/Fazer api and create new Menu object."""
import json
from apps.api.models import Menu
from . import sodexo


def create_menu(restaurant, d):
    """Create new  menu object."""
    menu = json.loads(sodexo.get_json(restaurant.id, d))
    courses = menu["courses"]
    new_menu = Menu.create(restaurant, d, courses)
    new_menu.save()
    return new_menu
