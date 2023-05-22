from django.db import models


class StatusOptions(models.TextChoices):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusOptions.choices,
        default=StatusOptions.todo,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tasks",
        blank=True,
        null=True,
    )
