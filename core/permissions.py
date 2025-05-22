from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsScrumMaster(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'scrum_master'


class IsProductOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'product_owner'


class IsDevelopper(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'developper'


class IsProductOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return (obj.owner == request.user) or (request.user.role == 'product_owner')
