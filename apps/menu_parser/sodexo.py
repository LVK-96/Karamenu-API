"""Get menus from Sodexo api."""
import requests
from .course import Course


def get_json(api_id, day):
    """Get menu as json."""
    # restaurant_id is already validated at view.
    url = f"https://www.sodexo.fi/ruokalistat/output/daily_json/{api_id}/{day.year}-{day:%m}-{day:%d}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def parse_courses(courses):
    parsed_courses = []
    for i in range(1, len(courses) + 1):
        course = courses[str(i)]
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
            tags = tags.replace(',', '')
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
