from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    problem = models.CharField(max_length=255, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title


