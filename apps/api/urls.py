"""Urlpatterns for api app."""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.api import views

urlpatterns = [
    path('restaurant/<int:restaurant>', views.RestaurantView),
    path('restaurant/<int:restaurant>/<int:day>/<int:month>/<int:year>',
         views.MenuView),
]

urlpatterns = format_suffix_patterns(urlpatterns)
