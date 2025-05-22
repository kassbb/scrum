from django.urls import path, include
from .views import BlocklogsViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'blocklogs', BlocklogsViewSet, basename='blocklogs')


urlpatterns = [
    path('', include(router.urls))
]
