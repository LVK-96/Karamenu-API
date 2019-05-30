"""Views for RESTful API."""
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restaurant  # TODO: Menu will be needed here later
from .serializers import RestaurantSerializer, MenuSerializer
from apps.menu_parser import sodexo


@api_view(['GET'])
def RestaurantView(request, format=None):
    """Retrieve restaurants."""
    if request.method == 'GET':
        restaurant = Restaurant.objects.get(pk=1)
        serializer = RestaurantSerializer(restaurant,
                                          context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def MenuView(request, format=None):
    """Retrieve menus."""
    
    if request.method == 'GET':
        menu = sodexo.create_menu()
        serializer = MenuSerializer(menu, context={'request': request})
        return Response(serializer.data)
