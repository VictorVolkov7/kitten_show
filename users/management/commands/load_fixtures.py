import os

from django.core.management import call_command, BaseCommand


class Command(BaseCommand):
    """Command to load all fixtures to database."""

    help = "Loads fixtures from fixtures dir"
    fixtures_dir = "fixtures"
    loaddata_command = "loaddata"
    filenames = (
        "users",
        "breeds",
        "kittens",
        "ratings",
    )

    def handle(self, *args, **options):
        for filename in self.filenames:
            call_command(
                self.loaddata_command,
                os.path.join(self.fixtures_dir, f"{filename}.json"),
            )
