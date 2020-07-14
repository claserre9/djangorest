from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow to modify only own profile"""

    def has_object_permission(self, request, view, obj):
        """detect if user make change to own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnPost(permissions.BasePermission):
    """Allow user to update own post"""
    def has_object_permission(self, request, view, obj):
        """Check if user try to update own post"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id