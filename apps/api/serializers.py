from apps.api.models import Restaurant, Menu
from rest_framework import serializers

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'address')

class MenuSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('date', 'url')
