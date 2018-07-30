
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Transaction
from django.contrib.auth import get_user_model

User = get_user_model()


class TransactionModelSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        depth = 1
        fields = [
            'id',
            'amount',
        ]
