import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Command to create new superuser."""

    def handle(self, *args, **options):
        admin = User.objects.create(
            email=os.getenv("SU_EMAIL"),
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )

        admin.set_password(os.getenv("SU_PASSWORD"))
        admin.save()
