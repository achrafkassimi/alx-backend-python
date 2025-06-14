# Django-Chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('message/<int:message_id>/history/', views.message_history_view, name='message-history'),
]
