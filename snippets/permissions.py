# Here for object level permissions , so as to make sure only the user that created a code snippet is able to update or delete it
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # custom permission to only allow owners of an object to edit it

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request, always allow GET,HEAD, or OPTIONS requests
        # return super().has_object_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # permissions are only allowed to the owner of the snippet
        return obj.owner == request.user
    