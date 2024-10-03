from django.contrib import admin

from breeds.models import Breed


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """
    Breed model for django admin.

    It is possible to search by breed.
    """

    list_display = (
        "pk",
        "breed_name",
        "description",
    )
    search_fields = ("breed_name",)
