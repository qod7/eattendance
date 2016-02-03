from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrganizationOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if(request.user):
            if(request.user.organization):
                return True

        return False

        # return obj.owner == request.user
