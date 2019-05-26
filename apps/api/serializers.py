"""Serializers for models."""
from apps.api.models import Restaurant, Menu
from rest_framework import serializers


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for restaurants."""

    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'opens', 'closes', 'url')


class MenuSerializer (serializers.HyperlinkedModelSerializer):
    """Serializer for menus."""

    class Meta:
        model = Menu
        fields = ('restaurant', 'date', 'url', 'courses')
