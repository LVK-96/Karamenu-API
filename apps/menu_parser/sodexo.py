"""Get menus from Sodexo api."""
import requests
from .api_lookup import lookup
from .course import Course


def get_json(restaurant_id, day):
    """Get menu as json."""
    # restaurant_id is already validated at view.
    sodexo_r = lookup[restaurant_id]
    url = ('https://www.sodexo.fi/ruokalistat/output'
           '/daily_json/{r}/{y}/{m}/{d}/fi')
    url = url.format(r=sodexo_r, y=day.year, m=day.month, d=day.day)
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.HTTPError:
        return "{}"


def parse_courses(courses):
    parsed_courses = []
    for course in courses:
        # TODO: refactor this :D
        try:
            name_fi = course["title_fi"]
        except KeyError:
            name_fi = ""
        
        try:
            name_en = course["title_en"]
        except KeyError:
            name_en = ""
        
        try:
            category = course["category"]
        except KeyError:
            category = ""
        
        try:
            price = course["price"]
        except KeyError:
            price = ""
        
        try:
            tags = course["properties"]
        except KeyError:
            tags = ""
        
        try:
            desc_fi = course["desc_fi"]
        except KeyError:
            desc_fi = ""
        try:
            desc_en = course["desc_en"]
        except KeyError:
            desc_en = ""

        parsed_course = Course(category, name_fi, name_en, desc_fi, desc_en,
                               tags, price)
        parsed_courses.append(parsed_course)

    return parsed_courses
