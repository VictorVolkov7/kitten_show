from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for User (create)."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")


class UserKittenSerializer(serializers.ModelSerializer):
    """Serializer for Kitten GET serializer."""

    class Meta:
        model = User
        fields = ("email",)
