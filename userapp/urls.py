from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('root', AuthorView, basename='author_views')


urlpatterns = [
    path('all/', GetUserView.as_view(), name="all_users"),
    path('add/', AddUserView.as_view(), name="add_new_user"),
    path('author/generate/', GenerateAuthorView.as_view(), name='generate_author'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('<int:id>/', UserGetView.as_view(), name='get_delete_user'),
    path('<int:id>/setsuper/', SetSuperView.as_view(), name='set_super'),
    path('<int:id>/setstaff/', SetStaffView.as_view(), name='set_staff'),
    path('author/all/', include(router.urls))
]