"""Views for RESTful API."""
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from apps.menu_parser.create_menu import create_menu


@api_view(['GET'])
def RestaurantView(request, restaurant, format=None):
    """Retrieve restaurants."""
    if request.method == 'GET':
        try:
            restaurant = Restaurant.objects.get(pk=restaurant)
        except ObjectDoesNotExist:
            content = {'Invalid restaurant id': restaurant}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        serializer = RestaurantSerializer(restaurant,
                                          context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def MenuView(request, restaurant, day, month, year, format=None):
    """Retrieve menus."""
    if request.method == 'GET':
        try:
            r = Restaurant.objects.get(pk=restaurant)
        except ObjectDoesNotExist:
            content = {'Invalid restaurant id': restaurant}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        try:
            d = date(year, month, day)
        except ValueError:
            content = {'Invalid date': "{d}.{m}.{y}".format(d=day,
                                                            m=month, y=year)}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        try:
            menu = Menu.objects.get(restaurant=r, date=d)
        except ObjectDoesNotExist:
            menu = create_menu(r, d)

        serializer = MenuSerializer(menu, context={'request': request})
        return Response(serializer.data)
