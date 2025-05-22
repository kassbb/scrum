from django.urls import resolve
from apps.users.views import UserRegisterCreateView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView


def test_register_url_resolves():
    assert resolve('/api/users/register/').func.view_class == UserRegisterCreateView


def test_ligin_url_resolves():
    assert resolve('/api/users/login/').func.view_class == TokenObtainPairView


def test_user_detail_url_resolves():
    match = resolve('/api/users/1/')
    assert match.func.view_class == UserDetailView
    assert match.kwargs['pk'] == 1
