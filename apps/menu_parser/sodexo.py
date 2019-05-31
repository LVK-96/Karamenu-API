"""Get menus from Sodexo api."""
import requests
import json
from datetime import date
from apps.api.models import Menu


def get_json(restaurant_id, day):
    """Get menu as json."""
    # TODO: create a lookup table to covert karamenu id to sodexo/fazer api id
    if restaurant_id == 1:
        sodexo_r = 27770
    elif restaurant_id == 2:
        sodexo_r = 35956
    else:
        sodexo_r = 0
    url = ('https://www.sodexo.fi/ruokalistat/output'
           '/daily_json/{r}/{y}/{m}/{d}/fi')
    url = url.format(r=sodexo_r, y=day.year, m=day.month, d=day.day)
    resp = requests.get(url)
    try:
        resp.raise_for_status()
        return resp.text
    except ValueError:
        return None


def create_menu(restaurant_id, day, month, year):
    """Create menu object."""
    d = date(year, month, day)
    menu = json.loads(get_json(restaurant_id, d))
    restaurant = menu["meta"]["ref_title"]
    courses = menu["courses"]
    new_menu = Menu.create(restaurant, d, courses)
    new_menu.save()
    return new_menu
