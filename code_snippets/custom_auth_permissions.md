# Custom Permission Classes in Django Restframework

This document will give a brief overview of how custom user permissions are created and used.

## Definition

```python
from rest_framework.permissions import BasePermission


class NewPermissionClass(BasePermission):
    '''
    Example of Custom Permission Class Definition
    '''
    def has_permission(self, request, view):
        return bool(
            condition_001 
            and|or condition_002...
            and|or condition_n
        )
```

## Usage

```python
from module.package.file import NewPermissionClass

class NewPermClassTest(APIView):
    '''
    View to test the key-auth:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [NewPermissionClass]

    def get(self, request):
        return Response(
            {
                "message": "You have successfully authenticated with the new custom permission class.",
            },
            status=status.HTTP_200_OK
        )
```

## Explanation

Suppose you have implemented a custom user model with the field `user_type`, where the values may be:
    `tier_1`, `tier_2`, `tier_3`,...
and so on.

Also, suppose you have an API called `XYZView` which you only want to be accessible by a certain type of user and no one else;
suppose you only want users of `user_type` == `tier_5`.

 _An example would be like how in a Social Media site, you only want the original author of a post to be able to edit it and no one else, not even an administrator of the site._ 
 
 _**This is only an example of the when you don't want to give admins some abilities, not a use-case of the matter at hand.**_

Now you can obviously write the conditions on every API where you want this enforced, but then you would have to write this condition in every API you want to enforce this in and since we are trying to follow D.R.Y while writing modern code, that approach would neither be logical, nor maintainable in the long term.

Instead, we can do the following:

### 1. Write a new Permission Class.

```python
from rest_framework.permissions import BasePermission


class IsTier5User(BasePermission):
    def has_permission(self, request, view):
        return bool(
                request.user.is_authenticated
                and request.user.user_type=="tier_5"
            )
```

And that is it for the new permission class; it is ready to be implemented as it will return `True` only if the user who initiated the request has a `user_type` of the value `tier_5` in the database. Notice how we also added a `request.user.is_authenticated` in the beginning; while this may not be strictly necessary, I personally consider it to just be good practice.

### 2. Implement the new Permission Class

```python
from module.package.file import IsTier5User

class XYZView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTier5User]

    def get(self, request):
        return Response(
            {
                "message": "You have successfully authenticated with the new custom permission class.",
            },
            status=status.HTTP_200_OK
        )
```
And with this, we have created a view that can only be accessed by users with `tier_5` as their `user_type`.
