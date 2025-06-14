from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.utils import timezone


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    # If the message is new (created is True), create a notification for the receiver
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )


@receiver(pre_save, sender=Message)
def save_message_history(sender, instance, **kwargs):
    try:
        original = Message.objects.get(id=instance.id)
        if original.content != instance.content:
            # Sauvegarder l'ancien contenu dans MessageHistory
            MessageHistory.objects.create(
                message=original,
                old_content=original.content
            )
            instance.edited_at = timezone.now()  # Set the timestamp when it was edited
            instance.edited_by = instance.sender  # Assuming the sender is editing the message, you can modify as needed
            instance.edited = True
    except Message.DoesNotExist:
        pass  # Pas de message original, donc rien à faire
