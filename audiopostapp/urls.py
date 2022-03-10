from django.urls import path, include
from audiopostapp.views import *

# Declare the paths here:

urlpatterns = [
    path('post/all', AudioPostView.as_view(), name="all_audio_posts"),
    
]