from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user and request.user.is_authenticated


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff
