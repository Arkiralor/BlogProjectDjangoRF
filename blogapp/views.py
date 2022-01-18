from turtle import update
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from userapp.models import Author, User
from userapp.serializers import AuthorSerializer
from .models import Blog, Tag
from .serializers import BlogPostSerializer, BlogSerializer, TagSerializer

# Create your views here.


class BlogView(APIView):
    '''
    View to GET all blog-posts and POST a new blog-post:
    '''

    def get(self, request):
        '''
        GET all blog-posts:
        '''
        queryset = Blog.objects.all()
        serialized = BlogSerializer(queryset, many=True)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )

    def post(self, request):
        '''
        POST a new blog-post:
        '''
        if request.user:
            author = Author.objects.filter(user=request.user).first()
            request.data["author"] = AuthorSerializer(author).data.get('id')
            
            deserialized = BlogSerializer(data=request.data)

            if deserialized.is_valid():
                deserialized.save()

                return Response(
                    deserialized.data,
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "error": str(deserialized.errors)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        elif not request.user:
            return Response(
                {
                    "error": "please login to add a new blog post."
                },
                status = status.HTTP_401_UNAUTHORIZED
            )


class BlogIndView(APIView):
    '''
    View to GET/PUT/DELETE individual blog-posts:
    '''

    def get(self, request, id: int):
        queryset = Blog.objects.get(pk=id)
        serialized = BlogPostSerializer(queryset)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )

    def put(self, request, id: int):
        blog_post = Blog.objects.get(pk=id)
        update = request.data

        updated = BlogPostSerializer(blog_post, data=update)

        if updated.is_valid():
            updated.save()
            return Response(
                updated.data,
                status=status.HTTP_202_ACCEPTED
            )
        else:
            return Response(
                {
                    "error": str(updated.errors)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id: int):
        try:
            blog_post = Blog.objects.get(pk=id)
            serialized = BlogPostSerializer(blog_post)

            blog_post.delete()

            return Response(
                serialized.data,
                status=status.HTTP_410_GONE
            )
        except Blog.DoesNotExist:
            return Response(
                {
                    "error": f"Blog with ID #{id} does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )


class TagView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
