from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #getmethod is safe
            return True
        return obj.owner == request.user #boolean the owner of the object and the user that is making the request. if they are the same, then it is true and theu do have object permission  but if inequal then they don't have permission
        