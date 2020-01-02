import json
import requests.exceptions
from unittest.mock import patch
from datetime import date
from django.test import TestCase
from django.core.management import call_command
from apps.api.models import Restaurant, Menu
from apps.menu_parser.course import Course
from apps.menu_parser.parse_menu import parse_menu
from apps.menu_parser.sodexo import parse_courses
from apps.menu_parser.serializers import CourseSerializer


class ParseMenuTest(TestCase):
    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)
        self.restaurant = Restaurant.objects.get(pk=2)
        self.day = date(2019, 5, 10)
        self.mock_json1 = open('apps/menu_parser/tests/'
                               'mock_response_sodexo.json', 'r').read()

    @patch('apps.menu_parser.parse_menu.sodexo.get_json')
    def test_no_response_from_api(self, mock_get_json):
        mock_get_json.side_effect = requests.exceptions.HTTPError
        not_available = Course("", "Ei saatavilla", "", "", "", "", "")
        courses = CourseSerializer([not_available], many=True).data
        correct_menu = Menu.create(self.restaurant, self.day, courses)
        self.assertEqual(parse_menu(self.restaurant, self.day), correct_menu)

    @patch('apps.menu_parser.parse_menu.sodexo.get_json')
    def test_correct_response_from_api(self, mock_get_json):
        mock_courses = parse_courses(json.loads(self.mock_json1)["courses"])
        mock_courses = CourseSerializer(mock_courses, many=True).data
        mock_menu = Menu.create(self.restaurant, self.day, mock_courses)
        mock_get_json.return_value = self.mock_json1
        self.assertEqual(parse_menu(self.restaurant, self.day), mock_menu)
