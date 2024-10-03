from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from breeds.serializers import BreedKittenSerializer
from kittens.models import Kitten
from ratings.serializers import RatingRetrieveSerializer
from users.serializers import UserKittenSerializer


class KittenListRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for Kitten (list/retrieve)."""

    full_age = serializers.SerializerMethodField(read_only=True)
    breed = BreedKittenSerializer(read_only=True)
    owner = UserKittenSerializer(read_only=True)
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Kitten
        fields = (
            "name",
            "full_age",
            "breed",
            "color",
            "description",
            "owner",
            "rating",
        )

    @staticmethod
    def get_full_age(obj) -> str:
        """
        Method for obtaining full age.

        The method checks the age values
        and returns the required string.
        :param obj: Kitten object
        :return: Full age str
        """
        years = obj.age_year
        months = obj.age_month

        if years is None:
            return f"{months} month{'s' if months > 1 else ''}"
        elif months is None:
            return f"{years} year{'s' if years > 1 else ''}"
        else:
            return (
                f"{years} year{'s' if years > 1 else ''} "
                f"and {months} month{'s' if months > 1 else ''}"
            )

    @staticmethod
    def get_rating(obj) -> list:
        """
        Method for gets rating list for kittens.

        :param obj: Kitten object
        :return: Rating list
        """
        rating_list = obj.kitten_ratings.all()
        serializer = RatingRetrieveSerializer(rating_list, many=True)
        return serializer.data


class KittenCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for Kitten (create/update)."""

    class Meta:
        model = Kitten
        fields = (
            "name",
            "age_year",
            "age_month",
            "breed",
            "color",
            "description",
            "owner",
        )
        read_only_fields = ("owner",)

    def validate(self, data):
        """
        Additional validation check.

        Checking that the age is specified
        in either years or months.
        """
        instance = self.instance

        if "age_year" in data:
            years = data["age_year"]
        else:
            years = instance.age_year

        if "age_month" in data:
            months = data["age_month"]
        else:
            months = instance.age_month

        if years is None and months is None:
            raise ValidationError(
                _("You must specify either the age in years or in months.")
            )
        return data
