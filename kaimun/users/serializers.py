
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'verification_completed',
            'date_joined',
            'last_login',
        ]
        read_only_fields = (
            'id',
            'password',

        )


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()
