from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Ticket
from api.serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user, worker=get_next_worker())

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Ticket.objects.all()
        elif self.request.user.is_staff:
            return Ticket.objects.filter(worker=self.request.user)
        else:
            return Ticket.objects.filter(creator=self.request.user)


def get_next_worker():
    workers = User.objects.filter(is_staff=True, is_superuser=False).annotate(num_requests=Count('worker'))
    workers = sorted(workers, key=lambda worker: worker.num_requests)
    return workers[0] if workers else None
