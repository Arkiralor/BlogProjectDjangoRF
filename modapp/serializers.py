from rest_framework import serializers

from modapp.models import ReportedPost
from blogapp.models import Blog
from blogapp.serializers import BlogPostSerializer


class ReportedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedPost
        fields = '__all__'
