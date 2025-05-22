from django.urls import path, include
from .views import SprintViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', SprintViewSet, basename='sprint')


urlpatterns = [
    path('', include(router.urls))
]
