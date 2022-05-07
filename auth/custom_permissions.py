from rest_framework.permissions import BasePermission
from userapp.models import Author


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


class HasAuthor(BasePermission):
    '''
    Allows access only to users with generated authors.
    '''

    def has_permission(self, request, view):
        author = Author.objects.get(user=request.user)
        return bool(
            author
            and request.user.is_authenticated
        )
