"""Urlpatterns for api app."""
from django.urls import path
from django.views.generic import RedirectView
from apps.api import views

urlpatterns = [
    path('restaurants', views.RestaurantsView),
    path('restaurants/', RedirectView.as_view(url='/restaurants')),
    path('restaurants/<int:restaurant>', views.RestaurantView),
    path('restaurants/<int:restaurant>/', RedirectView.as_view(url='restaurants/<int:restaurant>')),
    path('restaurants/<int:restaurant>/<int:day>/<int:month>/<int:year>',
         views.MenuView),
    path('restaurants/<int:restaurant>/<int:day>/<int:month>/<int:year>/', RedirectView.as_view(url='restaurants/<int:restaurant/<int:day>/<int:month>/<int:year>')),
]
