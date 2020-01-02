from unittest.mock import patch
import requests.exceptions
from datetime import date
from django.core.management import call_command
from django.test import TestCase
from apps.menu_parser.sodexo import get_json, parse_courses
from apps.menu_parser.course import Course
from apps.api.models import Restaurant


class TestSodexo(TestCase):
    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)
        self.restaurant = Restaurant.objects.get(pk=2)
        self.day = date(2019, 5, 10)
        self.mock_response = open('apps/menu_parser/tests/'
                                  'mock_response_sodexo.json', 'r').read()

    @patch('apps.menu_parser.sodexo.requests.get')
    def test_get_json(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = self.mock_response
        menu = get_json(self.restaurant.api_id, self.day)
        self.assertEqual(menu, self.mock_response)

    @patch('apps.menu_parser.sodexo.requests.get')
    def test_get_json_api_offline(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.ok = False
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            get_json(self.restaurant.api_id, self.day)

    def test_parse_courses(self):
        test_dict = {
            "1": {
                'title_fi': 'Paneroitu porsaanleike,'
                            'perunasosetta ja pippurikastike',
                'title_en': 'Breaded pork cutlet, mash potatoes and pepper sauce',
                'category': 'FROM THE KITCHEN',
                'price': '7,30 / 9,50',
                'properties': 'L',
                'desc_fi': 'gluteeiniton pyydettäessä',
                'desc_en': 'ask gluten free ',
                'desc_se': ''
            },
            "2": {
                'title_fi': 'Tomin erikoinen',
                'title_en': 'Toms special',
                'category': 'FROM THE ÄIJÄT :D',
                'price': '7,30 / 9,50',
                'properties': 'L',
                'desc_fi': 'RSÄ :D',
                'desc_en': 'ask gluten free ',
                'desc_se': ''
            }
        }


        correct_course1 = Course(test_dict["1"]['category'], test_dict["1"]['title_fi'],
                                 test_dict["1"]['title_en'], test_dict["1"]['desc_fi'],
                                 test_dict["1"]['desc_en'],
                                 test_dict["1"]['properties'], test_dict["1"]['price'])

        correct_course2 = Course(test_dict["2"]['category'], test_dict["2"]['title_fi'],
                                 test_dict["2"]['title_en'], test_dict["2"]['desc_fi'],
                                 test_dict["2"]['desc_en'],
                                 test_dict["2"]['properties'], test_dict["2"]['price'])
        correct_courses = [correct_course1, correct_course2]
        self.assertEqual(parse_courses(test_dict), correct_courses)
