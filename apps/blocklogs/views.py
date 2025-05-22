from rest_framework import viewsets
from .serializers import BlocklogsSerializer
from .models import Backlogs
from core.permissions import IsProductOwnerOrReadOnly


class BlocklogsViewSet(viewsets.ModelViewSet):
    queryset = Backlogs.objects.all()
    serializer_class = BlocklogsSerializer
    permission_classes = [IsProductOwnerOrReadOnly]
