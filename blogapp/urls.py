from django.urls import path, include
from .views import BlogView, BlogIndView, TagView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hashtags', TagView)

# Declare the paths here:

urlpatterns = [
    path('post/all', BlogView.as_view(), name="blog_posts"),
    path('post/<int:id>', BlogIndView.as_view(), name="blog_ind_view"),
    path('hashtags/', include(router.urls))
]
