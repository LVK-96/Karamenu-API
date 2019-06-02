"""Get menus from Sodexo api."""
import requests
import json
from apps.api.models import Menu
from .api_lookup import lookup


def get_json(restaurant_id, day):
    """Get menu as json."""
    # restaurant_id is already validated at view.
    sodexo_r = lookup[restaurant_id]
    url = ('https://www.sodexo.fi/ruokalistat/output'
           '/daily_json/{r}/{y}/{m}/{d}/fi')
    url = url.format(r=sodexo_r, y=day.year, m=day.month, d=day.day)
    resp = requests.get(url)
    try:
        resp.raise_for_status()
        return resp.text
    except ValueError:
        return None
