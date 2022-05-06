from django.urls import path, include
from modapp.views import GetAllReportedView

urlpatterns = [
    path('reported/all', GetAllReportedView.as_view(), name="all_reported_posts"),
]
