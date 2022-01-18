from django.urls import path, include
from .views import BlogView, BlogIndView, TagView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hashtags', TagView)

# Declare the paths here:

urlpatterns = [
    path('blog/post/all', BlogView.as_view(), name="blog_posts"),
    path('blog/post/<int:id>', BlogIndView.as_view(), name="blog_ind_view"),
    path('', include(router.urls))
]
