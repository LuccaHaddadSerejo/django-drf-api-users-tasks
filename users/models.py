from django.db import models
from django.contrib.auth.models import AbstractUser


class ProfileOptions(models.TextChoices):
    admin = "admin"
    manager = "manager"
    employee = "employee"


class User(AbstractUser):
    profile = models.CharField(
        max_length=20,
        choices=ProfileOptions.choices,
        default=ProfileOptions.employee,
    )
