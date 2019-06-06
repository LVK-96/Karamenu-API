"""Serializer for course."""
from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    """Serialize course objects to karamenu formated JSON."""

    category = serializers.CharField(max_length=100)
    name_fi = serializers.CharField(max_length=100)
    name_en = serializers.CharField(max_length=100)
    desc_fi = serializers.CharField(max_length=100)
    desc_en = serializers.CharField(max_length=100)
    tags = serializers.CharField(max_length=100)
    price = serializers.CharField(max_length=100)
