from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from ratings.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "get_kitten_name",
        "rating",
        "get_user_email",
    )
    search_fields = (
        "kitten__name",
        "user__email",
    )
    readonly_fields = ("user",)

    def get_user_email(self, obj):
        """
        Method for displaying a link instead of an id.

        :param obj: Kitten instance
        :return: user profile link as owner email
        """
        return mark_safe(
            f'<a href="{reverse("admin:users_user_change",
                                args=[obj.user.id])}">'
            f"{obj.user.email}</a>"
        )

    def get_kitten_name(self, obj):
        """
        Method for displaying a link instead of an id.

        :param obj: Kitten instance
        :return: breed link as breed name
        """
        return mark_safe(
            f'<a href="{reverse("admin:kittens_kitten_change",
                                args=[obj.kitten.id])}">'
            f"{obj.kitten.name}</a>"
        )

    def save_model(self, request, obj, form, change):
        """Addition for saving a rating."""
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    get_user_email.short_description = _("User email")
    get_kitten_name.short_description = _("Kitten name")
