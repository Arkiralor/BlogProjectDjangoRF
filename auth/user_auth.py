from rest_framework.permissions import BasePermission


class HasKeyAuth(BasePermission):
    '''
    Allows access only to users who have been assigned keys.
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.has_key)