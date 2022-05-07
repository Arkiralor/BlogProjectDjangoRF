from django.urls import path, include
from searchapp.views import SearchPostView

urlpatterns = [
    path('blog/', SearchPostView.as_view(), name="search_blog_posts"),
]