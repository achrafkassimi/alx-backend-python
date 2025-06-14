from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

class NotificationTestCase(TestCase):
    
    def setUp(self):
        # Creating two users
        self.sender = User.objects.create_user(username='sender', password='password')
        self.receiver = User.objects.create_user(username='receiver', password='password')

    def test_notification_creation(self):
        # Send a message from sender to receiver
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Hello, this is a test message!"
        )
        
        # Check if a notification has been created for the receiver
        notification = Notification.objects.filter(user=self.receiver, message=message).exists()
        self.assertTrue(notification)
        
    def test_no_notification_for_non_receiver(self):
        # Send a message from sender to receiver
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Another test message!"
        )
        
        # Check that no notification is created for the sender
        notification = Notification.objects.filter(user=self.sender, message=message).exists()
        self.assertFalse(notification)


class MessageTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_message_history(self):
        # Créer un message
        message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello!")
        # Modifier le message
        message.content = "Hello, how are you?"
        message.save()

        # Vérifier que l'historique du message est bien créé
        history = MessageHistory.objects.filter(message=message)
        self.assertEqual(history.count(), 1)
        self.assertEqual(history.first().old_content, "Hello!")
