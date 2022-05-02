from rest_framework.permissions import BasePermission


class HasKeyAuth(BasePermission):
    '''
    Allows access only to users who have been assigned keys.
    '''

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_key)


class IsModerator(BasePermission):
    '''
    Allows access only to moderators and superusers.
    '''

    def has_permission(self, request, view):
        is_true = (
            request.user.user_type == "moderator" 
            or request.user.is_staff
            )
        return bool(is_true and request.user.is_authenticated)
