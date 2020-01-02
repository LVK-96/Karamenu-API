import requests
from .course import Course


def get_json(api_id):
    """Get menu as json."""
    # TODO: Add support for English
    url = ('https://www.fazerfoodco.fi/modules/json/json/Index?costNumber={r}'
           '&language=fi')
    url = url.format(r=api_id)
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


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
        tags = tags.replace(',', '')
        parsed_course = Course("", name_fi, "", "", "", tags, "")
        parsed_courses.append(parsed_course)

    return parsed_courses
