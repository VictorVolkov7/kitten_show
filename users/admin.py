from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User model for django admin.

    It is possible to search by email and last_name.
    """

    list_display = (
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "email",
        "last_name",
    )
