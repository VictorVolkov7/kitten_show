from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Custom permission to checking the owner."""

    message = "You are not the owner of this object."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
