"""Views for RESTful API."""
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.api.models import Restaurant, Menu
from apps.api.serializers import RestaurantSerializer, MenuSerializer


@api_view(['GET'])
def restaurants(request, format=None):
    """Retrieve restaurants."""
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants)
        return Response(serializer.data)


@api_view(['GET'])
def menus(request, format=None):
    """Retrieve menus."""
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
