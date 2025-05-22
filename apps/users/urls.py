
from django.urls import path

from apps.users.views import UserRegisterCreateView, UserListView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/', UserDetailView.as_view(), name="user-detail"),
    path('users/', UserListView.as_view(), name="user-list")
]
