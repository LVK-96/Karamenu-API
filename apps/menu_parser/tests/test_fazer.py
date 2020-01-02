import json
from unittest.mock import patch
import requests.exceptions
from datetime import date
from django.core.management import call_command
from django.test import TestCase
from apps.menu_parser.fazer import get_json, parse_courses
from apps.menu_parser.course import Course
from apps.api.models import Restaurant


class TestFazer(TestCase):
    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)
        self.restaurant = Restaurant.objects.get(pk=3)
        self.mock_response = open('apps/menu_parser/tests/'
                                  'mock_response_fazer.json', 'r').read()

    @patch('apps.menu_parser.fazer.requests.get')
    def test_get_json(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = self.mock_response
        menu = get_json(self.restaurant.api_id)
        self.assertEqual(menu, self.mock_response)

    @patch('apps.menu_parser.fazer.requests.get')
    def test_get_json_api_offline(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.ok = False
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            get_json(self.restaurant.api_id)

    def test_parse_courses(self):
        tmp = json.loads(self.mock_response)
        test_menu = tmp["MenusForDays"][0]["SetMenus"]
        correct_course1 = Course('',
                                 'testi-ruoka',
                                 '', '', '', 'A G L VS', '')

        self.assertEqual(parse_courses(test_menu), [correct_course1])
