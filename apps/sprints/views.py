from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import SprintSerializer
from .models import Sprint
from apps.users.permissions import IsSelf


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [IsSelf, IsAuthenticated]
