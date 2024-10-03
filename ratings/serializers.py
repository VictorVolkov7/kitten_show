from rest_framework import serializers

from kittens.models import Kitten
from ratings.models import Rating
from users.serializers import UserKittenSerializer


class RatingKittenSerializer(serializers.ModelSerializer):
    """Serializer for Rating."""

    class Meta:
        model = Kitten
        fields = ("name",)


class RatingCreateSerializer(serializers.ModelSerializer):
    """Serializer for Rating (create)."""

    class Meta:
        model = Rating
        fields = (
            "rating",
            "user",
            "kitten",
        )
        read_only_fields = (
            "user",
            "kitten",
        )


class RatingRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for Rating (retrieve)."""

    user = UserKittenSerializer(read_only=True)
    kitten = RatingKittenSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ("rating", "user", "kitten")
