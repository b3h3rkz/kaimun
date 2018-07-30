from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
)
from .models import Country


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'iso_code', 'currency', 'active']
