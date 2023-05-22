from django.db import models
from django.contrib.auth.models import AbstractUser


class ProfileOptions(models.TextChoices):
    admin = "Admin"
    manager = "Manager"
    employee = "Employee"


class User(AbstractUser):
    profile = models.CharField(
        max_length=20,
        choices=ProfileOptions.choices,
        default=ProfileOptions.employee,
    )
