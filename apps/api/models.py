"""Models for restaurants and menus."""
from django.db import models
from django.contrib.postgres.fields import JSONField


class Restaurant(models.Model):
    """Model for restaurant."""

    NA = 'NA'
    SODEXO = 'SDX'
    FAZER = 'FZR'
    COMPANY_CHOICES = [
            (NA, 'Not available'),
            (SODEXO, 'Sodexo'),
            (FAZER, 'Fazer')
    ]
    company = models.CharField(max_length=3, choices=COMPANY_CHOICES,
                               default=NA)
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    opens = models.TimeField(blank=True)
    closes = models.TimeField(blank=True)
    url = models.URLField(blank=True, default='')

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
