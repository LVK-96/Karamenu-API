"""Test views by checking the HTTP resonse codes."""
from unittest.mock import patch
from datetime import date
from django.test import TestCase
from django.core.management import call_command
from apps.api.models import Restaurant, Menu


class RestaurantViewTests(TestCase):
    """Test restaurant view."""

    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)

    def test_get_valid_restaurant_response(self):
        response = self.client.get('/restaurants/1')
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_id_restaurant_response(self):
        response = self.client.get('/restaurants/asd')
        self.assertEqual(response.status_code, 404)

    def test_options_restaurant_response(self):
        response = self.client.options('/restaurants/1')
        self.assertEqual(response.status_code, 200)

    # Test that only GET and OPTIONS are allowed
    def test_post_restaurant_response(self):
        response = self.client.post('/restaurants/1')
        self.assertEqual(response.status_code, 405)

    def test_put_restaurant_response(self):
        response = self.client.put('/restaurants/1')
        self.assertEqual(response.status_code, 405)

    def test_delete_restaurant_response(self):
        response = self.client.delete('/restaurants/1')
        self.assertEqual(response.status_code, 405)

    def test_head_restaurant_response(self):
        response = self.client.head('/restaurants/1')
        self.assertEqual(response.status_code, 405)

    def test_patch_restaurant_response(self):
        response = self.client.patch('/restaurants/1')
        self.assertEqual(response.status_code, 405)


class MenuViewTests(TestCase):
    """Test Menu view."""

    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)

    @patch('apps.api.views.parse_menu')
    def test_get_valid_menu_response(self, mock_parse_menu):
        restaurant = Restaurant.objects.get(pk=1)
        mock_menu = Menu.create(restaurant, date(2019, 5, 10), '')
        mock_parse_menu.return_value = mock_menu  # Mock parse_menu()
        response = self.client.get('/restaurants/1/5/6/2019')
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_id_menu_response(self):
        response = self.client.get('/restaurants/asd/1/5/2019')
        self.assertEqual(response.status_code, 404)

    def test_get_invalid_date_menu_response(self):
        response = self.client.get('/restaurants/1/100/1/2019')
        self.assertEqual(response.status_code, 404)

    def test_options_menu_response(self):
        response = self.client.options('/restaurants/1/5/6/2019')
        self.assertEqual(response.status_code, 200)

    # Test that only GET and OPTIONS are allowed
    def test_post_menu_response(self):
        response = self.client.post('/restaurants/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_put_menu_response(self):
        response = self.client.put('/restaurants/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_delete_menu_response(self):
        response = self.client.delete('/restaurants/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_head_menu_response(self):
        response = self.client.head('/restaurants/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_patch_menu_response(self):
        response = self.client.patch('/restaurants/1/5/6/2019')
        self.assertEqual(response.status_code, 405)
