"""Models for restaurants and menus."""
from django.db import models
from django.contrib.postgres.fields import JSONField


class Restaurant(models.Model):
    """Model for restaurant."""

    company = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    opens = models.TimeField(blank=True)
    closes = models.TimeField(blank=True)
    url = models.URLField(blank=True, default='')
    api_id = models.CharField(max_length=100, default='')

    @classmethod
    def create(cls, name, address, opens, closes, url):
        """Create Restaurant object."""
        restaurant = cls(name=name, address=address,
                         opens=opens, closes=closes, url=url)
        return restaurant


class Menu(models.Model):
    """Model for menu."""

    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    courses = JSONField()

    @classmethod
    def create(cls, restaurant, date, courses):
        """Create Menu object."""
        menu = cls(restaurant=restaurant, date=date, courses=courses)
        return menu

    def __eq__(self, other):
        """For parse_menu"""
        return (self.restaurant == other.restaurant and self.date == other.date
                and self.courses == other.courses)
