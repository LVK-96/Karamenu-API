"""Test HTTP resonse codes."""

from django.test import TestCase
from django.core.management import call_command


class RestaurantViewTests(TestCase):
    """Test restaurant view."""

    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)

    def test_get_valid_restaurant_response(self):
        response = self.client.get('/restaurant/1')
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_id_restaurant_response(self):
        response = self.client.get('/restaurant/asd')
        self.assertEqual(response.status_code, 404)

    def test_options_restaurant_response(self):
        response = self.client.options('/restaurant/1')
        self.assertEqual(response.status_code, 200)

    # Test that only GET and OPTIONS are allowed
    def test_post_restaurant_response(self):
        response = self.client.post('/restaurant/1')
        self.assertEqual(response.status_code, 405)

    def test_put_restaurant_response(self):
        response = self.client.put('/restaurant/1')
        self.assertEqual(response.status_code, 405)

    def test_delete_restaurant_response(self):
        response = self.client.delete('/restaurant/1')
        self.assertEqual(response.status_code, 405)

    def test_head_restaurant_response(self):
        response = self.client.head('/restaurant/1')
        self.assertEqual(response.status_code, 405)

    def test_patch_restaurant_response(self):
        response = self.client.patch('/restaurant/1')
        self.assertEqual(response.status_code, 405)


class MenuViewTests(TestCase):
    """Test Menu view."""

    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)

    def test_get_valid_menu_response(self):
        response = self.client.get('/restaurant/1/5/6/2019')
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_id_menu_response(self):
        response = self.client.get('/restaurant/asd/1/5/2019')
        self.assertEqual(response.status_code, 404)

    def test_get_invalid_date_menu_response(self):
        response = self.client.get('/restaurant/1/100/1/2019')
        self.assertEqual(response.status_code, 404)
    
    def test_options_menu_response(self):
        response = self.client.options('/restaurant/1/5/6/2019')
        self.assertEqual(response.status_code, 200)

    # Test that only GET and OPTIONS are allowed
    def test_post_menu_response(self):
        response = self.client.post('/restaurant/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_put_menu_response(self):
        response = self.client.put('/restaurant/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_delete_menu_response(self):
        response = self.client.delete('/restaurant/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_head_menu_response(self):
        response = self.client.head('/restaurant/1/5/6/2019')
        self.assertEqual(response.status_code, 405)

    def test_patch_menu_response(self):
        response = self.client.patch('/restaurant/1/5/6/2019')
        self.assertEqual(response.status_code, 405)
