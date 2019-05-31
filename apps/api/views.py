"""Views for RESTful API."""
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restaurant  # TODO: Menu will be needed here later
from .serializers import RestaurantSerializer, MenuSerializer
from apps.menu_parser import sodexo


@api_view(['GET'])
def RestaurantView(request, restaurant, format=None):
    """Retrieve restaurants."""
    if request.method == 'GET':
        restaurant = Restaurant.objects.get(pk=restaurant)
        serializer = RestaurantSerializer(restaurant,
                                          context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def MenuView(request, restaurant, day, month, year, format=None):
    """Retrieve menus."""
    if request.method == 'GET':
        menu = sodexo.create_menu(restaurant, day, month, year)
        serializer = MenuSerializer(menu, context={'request': request})
        return Response(serializer.data)
