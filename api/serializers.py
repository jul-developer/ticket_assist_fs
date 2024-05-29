from rest_framework import serializers

from api.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = '__all__'
