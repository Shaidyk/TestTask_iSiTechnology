from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class ChatThread(models.Model):
    participants = models.ManyToManyField(User, related_name='threads')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.pk and self.participants.count() > 2:
            raise ValidationError("Thread can't have more than 2 participants.")

    def __str__(self):
        if not self.pk:
            return "Thread (unsaved)"
        return f"Thread between {', '.join([user.username for user in self.participants.all()])}"
