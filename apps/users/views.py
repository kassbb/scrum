from rest_framework import generics
from rest_framework.permissions import AllowAny
from .permissions import IsSelf
from apps.users.models import User
from apps.users.serializers import UserSerializer
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.utils.logging import handle_create_view


class UserRegisterCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_create_view(self, request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelf]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
