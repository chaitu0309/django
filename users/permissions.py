from rest_framework import permissions


class IsHUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, customer):
        if request.user:
            return customer == request.user
        return False
