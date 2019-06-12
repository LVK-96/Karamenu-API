
from unittest.mock import patch
from datetime import date
from django.core.management import call_command
from django.test import TestCase
from apps.menu_parser.sodexo import get_json, parse_courses
from apps.menu_parser.course import Course


class TestSodexo(TestCase):
    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)
        self.restaurant = 1
        self.day = date(2019, 5, 10)
        self.mock_response = open('apps/menu_parser/tests/'
                                  'mock_api_response.json', 'r').read()
    
    @patch('apps.menu_parser.sodexo.requests.get')
    def test_get_json(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = self.mock_response
        menu = get_json(self.restaurant, self.day)
        self.assertEqual(menu, self.mock_response)
    
    def test_parse_courses(self):
        test_dict1 = {
            'title_fi': 'Paneroitu porsaanleike,'
                        'perunasosetta ja pippurikastike',
            'title_en': 'Breaded pork cutlet, mash potatoes and pepper sauce',
            'category': 'FROM THE KITCHEN',
            'price': '7,30 / 9,50',
            'properties': 'L',
            'desc_fi': 'gluteeiniton pyydettäessä',
            'desc_en': 'ask gluten free ',
            'desc_se': ''
        }

        test_dict2 = {
            'title_fi': 'Tomin erikoinen',
            'title_en': 'Toms special',
            'category': 'FROM THE ÄIJÄT :D',
            'price': '7,30 / 9,50',
            'properties': 'L',
            'desc_fi': 'RSÄ :D',
            'desc_en': 'ask gluten free ',
            'desc_se': ''
        }

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
