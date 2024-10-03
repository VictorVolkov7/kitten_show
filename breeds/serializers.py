from rest_framework import serializers

from breeds.models import Breed


class BreedListSerializer(serializers.ModelSerializer):
    """Serializer for Breed (list_view)."""

    class Meta:
        model = Breed
        fields = ("breed_name", "description")


class BreedKittenSerializer(serializers.ModelSerializer):
    """Serializer for Kitten GET serializer."""

    class Meta:
        model = Breed
        fields = ("breed_name",)
