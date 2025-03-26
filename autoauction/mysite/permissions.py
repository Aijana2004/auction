from rest_framework import permissions


class CheckCreateCar(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'owner':
            return True
        return False


class CheckOwnerCar(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.car.seller


class CheckCreateBid(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'client':
            return True
        return False


class CheckOwnerBid(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.buyer


