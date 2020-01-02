import requests
import apps.menu_parser.api_lookup as api_lookup
from .course import Course


def get_json(api_id):
    """Get menu as json."""
    # TODO: Add support for English
    url = ('https://www.fazerfoodco.fi/modules/json/json/Index?costNumber={r}'
           '&language=fi')
    url = url.format(r=api_id)
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.HTTPError:
        return "{}"


def parse_courses(courses):
    try:
        cs = courses[0]["Components"]
    except IndexError:
        return None

    parsed_courses = []
    for course in cs:
        tmp = course.split(" (")
        name_fi = tmp[0]
        tags = tmp[1][:-1]  # Drop last ")" from string
        parsed_course = Course("", name_fi, "", "", "", tags, "")
        parsed_courses.append(parsed_course)

    return parsed_courses
