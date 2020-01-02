"""Test models."""

from datetime import date, time
from django.test import TestCase
from apps.api.models import Restaurant, Menu


class RestaunrantTests(TestCase):
    def setUp(self):
        self.name = "test_name"
        self.address = "test_address"
        self.opens = time(10, 30)
        self.closes = time(11, 30)
        self.url = "test.kivikunnas.xyz"
        self.restaurant = Restaurant.create(self.name, self.address,
                                            self.opens, self.closes, self.url)

    def test_name(self):
        self.assertEqual(self.name, self.restaurant.name)

    def test_address(self):
        self.assertEqual(self.address, self.restaurant.address)

    def test_opens(self):
        self.assertEqual(self.opens, self.restaurant.opens)

    def test_closes(self):
        self.assertEqual(self.closes, self.restaurant.closes)

    def test_url(self):
        self.assertEqual(self.url, self.restaurant.url)


class MenuTests(TestCase):
    def setUp(self):
        name = "test_name"
        address = "test_address"
        opens = time(10, 30)
        closes = time(11, 30)
        url = "test.kivikunnas.xyz"
        self.restaurant = Restaurant.create(name, address, opens, closes, url)
        self.date = date(2019, 5, 10)
        self.courses = []
        self.menu = Menu.create(self.restaurant, self.date, self.courses)

    def test_restaurant(self):
        self.assertEqual(self.restaurant, self.menu.restaurant)

    def test_date(self):
        self.assertEqual(self.date, self.menu.date)

    def test_courses(self):
        self.assertEqual(self.courses, self.menu.courses)
