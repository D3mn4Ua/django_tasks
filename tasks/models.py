from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Status(models.TextChoices):
        DONE = "DONE", "done"
        PROCESSING = "PROCESSING", "processing"
        NO_WORK = "NO WORK", "no work"

    status = models.CharField(max_length=63, choices=Status.choices, default=Status.NO_WORK)
    title = models.CharField(max_length=63)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return title