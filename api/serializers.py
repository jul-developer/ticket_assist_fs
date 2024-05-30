from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import serializers

from api.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        read_only_fields = (
            'creator', 'worker',
        )
        fields = '__all__'
