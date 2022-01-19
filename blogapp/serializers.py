from rest_framework import serializers
from .models import Blog, Tag

# Create your serializers here:


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'published', 'author', 'tags']


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
