""" Permissions """

from rest_framework.permissions import BasePermission, SAFE_METHODS


# Create your permissions here.
class IsOwner(BasePermission):
    """Check if the current logged in user is the owner of the object"""

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user == obj.user


class IsReadOnly(BasePermission):
    """Allow only if the request is read only"""

    def has_permission(self, request, view) -> bool:
        return request.method in SAFE_METHODS
