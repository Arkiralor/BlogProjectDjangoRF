from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('author', AuthorView)


urlpatterns = [
    path('all/', GetUserView.as_view(), name="all_users"),
    path('add/', AddUserView.as_view(), name="add_new_user"),
    path('author/generate/', GenerateAuthorView.as_view(), name='generate_author'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('authors/root', include(router.urls))
]