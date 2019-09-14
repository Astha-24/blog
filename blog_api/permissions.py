from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStory(permissions.BasePermission):
    """Allows user to update their own story"""

    def has_object_permission(self,request,view,obj):
        """Check the user is trying to update their own story"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author.id == request.user.id
