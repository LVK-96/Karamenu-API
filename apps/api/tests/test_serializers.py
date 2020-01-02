"""Test serializers."""

from django.test import TestCase
from django.core.management import call_command
from apps.api.models import Restaurant, Menu
from apps.api.serializers import RestaurantSerializer, MenuSerializer


class RestaurantSerializerTests(TestCase):
    """Test Restaurant serializer."""

    def setUp(self):
        call_command('loaddata', 'apps/api/fixtures/restaurants.json',
                     verbosity=0)
        self.restaurant = Restaurant.objects.get(pk=1)
        serializer = RestaurantSerializer(instance=self.restaurant)
        self.serializer_data = serializer.data

    def test_contains_correct_fields(self):
        self.assertCountEqual(self.serializer_data.keys(),
                              ['company', 'name', 'address',
                               'opens', 'closes', 'url', 'id'])

    def test_company_content(self):
        self.assertEqual(self.serializer_data['company'],
                         self.restaurant.company)

    def test_name_content(self):
        self.assertEqual(self.serializer_data['name'], self.restaurant.name)

    def test_address_content(self):
        self.assertEqual(self.serializer_data['address'],
                         self.restaurant.address)

    def test_opens_content(self):
        self.assertEqual(self.serializer_data['opens'], self.restaurant.opens.
                         strftime("%H:%M:%S"))

    def test_closes_content(self):
        self.assertEqual(self.serializer_data['closes'], self.restaurant.closes.
                         strftime("%H:%M:%S"))

    def test_url_content(self):
        self.assertEqual(self.serializer_data['url'], self.restaurant.url)


class MenuSerializerTests(TestCase):
    """Test Menu serializer."""

    def setUp(self):
        call_command('loaddata', 'apps/api/tests/test_data.json',
                     verbosity=0)
        self.menu = Menu.objects.get(pk=1)
        self.serializer = MenuSerializer(instance=self.menu)
        self.serializer_data = self.serializer.data

    def test_contains_correct_fields(self):
        self.assertCountEqual(self.serializer_data.keys(),
                              ['restaurant', 'date', 'courses'])

    def test_restaurant_content(self):
        restaurant = RestaurantSerializer(self.menu.restaurant)
        self.assertEqual(self.serializer_data['restaurant'], restaurant.data)

    def test_date_content(self):
        self.assertEqual(self.serializer_data['date'], self.menu.date
                         .strftime("%Y-%m-%d"))

    def test_courses_content(self):
        self.assertEqual(self.serializer_data['courses'], self.menu.courses)
