from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import filterProject
from core.permissions import IsProductOwnerOrReadOnly

from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProductOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = filterProject
