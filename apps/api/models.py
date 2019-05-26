from django.db import models
from django.contrib.postgres.fields import JSONField
from djmoney.models.fields import MoneyField

class Restaurant(models.Model):
    name = models.CharField(max_length = 100, blank = True, default = '')
    address = models.CharField(max_length = 100, blank = True, default = '') 
    opens = models.TimeField(blank = True)
    closes = models.TimeField(blank = True) 
    url = models.URLField(blank = True, default = '')

class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete = models.CASCADE) 
    date = models.DateField(blank = True)
    url = models.URLField(blank = True, default = '')
    courses = JSONField()
