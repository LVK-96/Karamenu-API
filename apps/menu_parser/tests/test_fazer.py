from unittest.mock import patch
from requests.exceptions import HTTPError
from datetime import date
from django.core.management import call_command
from django.test import TestCase
from apps.menu_parser.fazer import get_json, parse_courses
from apps.menu_parser.course import Course


class TestFazer(TestCase):
    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)
        self.restaurant = "Dreams Cafe"
        self.day = date(2019, 6, 19)
        self.mock_response = open('apps/menu_parser/tests/'
                                  'mock_response_fazer.json', 'r').read()
    
    @patch('apps.menu_parser.sodexo.requests.get')
    def test_get_json(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = self.mock_response
        menu = get_json(self.restaurant, self.day)
        self.assertEqual(menu, self.mock_response)
    
    @patch('apps.menu_parser.sodexo.requests.get')
    def test_get_json_api_offline(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.ok = False
        mock_get.return_value.raise_for_status.side_effect = HTTPError()
        menu = get_json(self.restaurant, self.day)
        self.assertEqual(menu, "{}")
    
    def test_parse_courses(self):
        test_dict1 = {
            'SortOrder': 0,
            'Name': 'Lounas',
            'Price': None,
            'Components': [
                "Broileria cashewpähkinä-jogurttikastikkeessa (A ,G ,L ,VS)"
            ]
        }

        test_dict2 = {
            "SortOrder": 0,
            "Name": "Kasvisruoka",
            "Price": None,
            "Components": [
                "Kasviskiusausta (A ,G ,L)",
                "Kasvis-herkkusienikiusausta (* ,A ,G ,L ,VS)"
            ]
        }
        # TODO: CONTINUE FROM HERE
        test_list = [test_dict1, test_dict2]

        correct_course1 = Course(test_dict1['category'], test_dict1['title_fi'],
                                 test_dict1['title_en'], test_dict1['desc_fi'],
                                 test_dict1['desc_en'],
                                 test_dict1['properties'], test_dict1['price'])

        correct_course2 = Course(test_dict2['category'], test_dict2['title_fi'],
                                 test_dict2['title_en'], test_dict2['desc_fi'],
                                 test_dict2['desc_en'],
                                 test_dict2['properties'], test_dict2['price'])
        correct_courses = [correct_course1, correct_course2]
        self.assertEqual(parse_courses(test_list), correct_courses)
