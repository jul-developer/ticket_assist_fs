from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    problem = models.CharField(max_length=255, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator')
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='worker', null=True)

    def __str__(self):
        return self.title
