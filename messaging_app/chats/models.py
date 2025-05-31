from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    user model
    """
    pass

class Conversation(models.Model):
    """
    Tracks which users are involved in a conversation
    """
    pass

class Message(models.Model):
    """
    message model
    """
    sender = models.ForeignKey(CustomUser)
    conversation = models.ForeignKey(conversation)