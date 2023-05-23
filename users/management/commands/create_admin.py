from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin user"

    def add_arguments(self, parser):
        ...
        parser.add_argument(
            "-u",
            "--username",
            type=str,
            help="Define the admin username",
        ),

        parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="Define the admin password",
        ),

    def handle(self, *args: tuple, **kwargs: dict):
        username = kwargs["username"]
        password = kwargs["password"]

        if not username:
            username = "admin"
        if not password:
            password = "admin1234"

        try:
            User.objects.get(username__exact=username)
            raise CommandError(f"Username `{username}` already taken.")
        except User.DoesNotExist:
            pass

        User.objects.create_superuser(
            username=username, password=password, profile="admin"
        )
        self.stdout.write(
            self.style.SUCCESS(f"Admin `{username}` successfully created!")
        )
