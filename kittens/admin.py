from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from kittens.models import Kitten


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    """
    Kitten model for django admin.

    It is possible to search by name, breed and owner email
    and filter by breed. With methods to display information
    instead of id.
    """

    list_display = (
        "pk",
        "name",
        "age_year",
        "age_month",
        "get_breed_name",
        "color",
        "get_owner_email",
    )
    search_fields = (
        "name",
        "breed__name",
        "owner__email",
    )
    list_filter = ("breed",)
    readonly_fields = ("owner",)

    def get_owner_email(self, obj):
        """
        Method for displaying a link instead of an id.

        :param obj: Kitten instance
        :return: user profile link as owner email
        """
        return mark_safe(
            f'<a href="{reverse("admin:users_user_change",
                                args=[obj.owner.id])}">'
            f"{obj.owner.email}</a>"
        )

    def get_breed_name(self, obj):
        """
        Method for displaying a link instead of an id.

        :param obj: Kitten instance
        :return: breed link as breed name
        """
        return mark_safe(
            f'<a href="{reverse("admin:breeds_breed_change",
                                args=[obj.breed.id])}">'
            f"{obj.breed.breed_name}</a>"
        )

    def save_model(self, request, obj, form, change):
        """Addition for saving a kitten."""
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    get_owner_email.short_description = _("Owner email")
    get_breed_name.short_description = _("Kitten breed")
