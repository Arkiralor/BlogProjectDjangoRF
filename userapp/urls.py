from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('users', UserView)
router.register('authors', AuthorView)


urlpatterns = [
    path('users/', UserView.as_view(), name="all_users"),
    path('', include(router.urls))
]