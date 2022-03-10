from rest_framework import serializers
from .models import Language, Blog, Tag

# Create your serializers here:

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    
    language = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'language', 'published', 'author', 'tags', 'genre']


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
