from django.contrib.auth.models import User
from django.db import models

from .chat_thread_model import ChatThread


class ChatMessage(models.Model):
    thread = models.ForeignKey(ChatThread, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} in thread {self.thread.id}"
