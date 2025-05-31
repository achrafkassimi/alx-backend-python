from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add any additional fields here
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Conversation(models.Model):
    participants = models.ManyToManyField('User', related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        participant_usernames = ", ".join([user.username for user in self.participants.all()])
        return f"Conversation between: {participant_usernames}"


class Message(models.Model):
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"
