"""Get menus from Sodexo api."""
import requests
import json
from datetime import date
from apps.api.models import Menu


def get_json(day):
    """Get menu as json."""
    url = ('https://www.sodexo.fi/ruokalistat/output'
           '/daily_json/27770/{y}/{m}/{d}/fi')
    url = url.format(y=day.year, m=day.month, d=day.day)
    r = requests.get(url)
    try:
        r.raise_for_status()
        return r.text
    except ValueError:
        return None


def create_menu():
    """Create menu object."""
    day = date.today()
    menu = json.loads(get_json(day))
    restaurant = menu["meta"]["ref_title"]
    courses = menu["courses"]
    new_menu = Menu.create(restaurant, day, courses)
    new_menu.save()
    return new_menu
