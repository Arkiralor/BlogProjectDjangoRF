from django.urls import path, include
from blogapp.views import BlogView, TagView, AddPostView, BlogIndView, ReportPostView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hashtags', TagView)

# Declare the paths here:

urlpatterns = [
    path('post/all', BlogView.as_view(), name="all_blog_posts"),
    path('post/new', AddPostView.as_view(), name="add_blog_post"),
    path('post/<int:id>', BlogIndView.as_view(), name="blog_ind_view"),
    path('post/report', ReportPostView.as_view(), name="report_post"),
    path('hashtags/', include(router.urls))
]
