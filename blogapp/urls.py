from django.urls import path, include
from blogapp.views import BlogView, TagView, AddPostView, BlogIndView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hashtags', TagView)

# Declare the paths here:

urlpatterns = [
    path('post/all', BlogView.as_view(), name="all_blog_posts"),
    path('post/new', AddPostView.as_view(), name="add_blog_post"),
    path('post/<int:id>', BlogIndView.as_view(), name="blog_ind_view"),
    path('hashtags/', include(router.urls))
]
