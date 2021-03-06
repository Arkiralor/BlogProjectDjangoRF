from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from userapp.models import Author, User
from userapp.serializers import AuthorSerializer, UserAdminSerializer
from .models import Blog, Tag
from .serializers import BlogPostSerializer, BlogInSerializer, BlogOutSerializer, TagSerializer
from .utils import TagUtils, LanguageUtils
from modapp.models import ReportedPost
from modapp.serializers import ReportedPostSerializer

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
        serialized = BlogOutSerializer(queryset, many=True)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )


class AddPostView(APIView):
    '''
    View to POST a new blog-post:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        '''
        POST a new blog-post:
        '''
        try:
            author = Author.objects.filter(user=request.user).first()
            if author is None:
                return Response(
                    {
                        "error": f"No author in system for user: {request.user}. Generate an author first."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            request.data["author"] = AuthorSerializer(author).data.get('id')
        except Author.DoesNotExist:
            return Response(
                {
                    "error": f"No author in system for user: {request.user}. Generate an author first."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.data.get("tags") is not None:
            tags = TagUtils(request.data["tags"])
            # Emptying the key-value pair to remove duplicate values.
            request.data["tags"] = None
            # Replace the hashtags with their IDs.
            request.data["tags"] = tags.resolve_tags()

        language_detector = LanguageUtils(request.data.get("body"))
        if request.data.get("language") is None:
            lang = language_detector.detect_language()
            request.data["language"] = language_detector.enter_language(lang)
        else:
            request.data["language"] = language_detector.enter_language(
                request.data.get("language"))

        deserialized = BlogInSerializer(data=request.data)

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


class BlogIndView(APIView):
    '''
    View to GET/PUT/DELETE individual blog-posts:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id: int):
        '''
        Get individual blog-post:
        '''
        try:
            queryset = Blog.objects.get(pk=id)
        except Blog.DoesNotExist:
            return Response(
                {
                    "error": f"Blog with ID #{id} does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serialized = BlogPostSerializer(queryset)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )

    def put(self, request, id: int):
        '''
        Update individual blog-post:
        '''
        blog_post = Blog.objects.get(pk=id)
        if request.user == blog_post.author.user or request.user.is_superuser:
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
        elif request.user != blog_post.author.user and not request.user.is_superuser:
            return Response(
                {
                    "error": f"you do not have permission to execute this ({__name__}) action."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

    def delete(self, request, id: int):
        '''
        Delete individual blog-post:
        '''
        try:
            blog_post = Blog.objects.get(pk=id)
            serialized = BlogPostSerializer(blog_post)

            if request.user == blog_post.author.user or request.user.is_superuser:
                blog_post.delete()

                return Response(
                    serialized.data,
                    status=status.HTTP_410_GONE
                )
            elif request.user != blog_post.user and not request.user.is_superuser:
                return Response(
                    {
                        "error": f"you do not have permission to execute this ({__name__}) action."
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Blog.DoesNotExist:
            return Response(
                {
                    "error": f"Blog with ID #{id} does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ReportPostView(APIView):
    '''
    View to report a BlogPost
    '''
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(request):
        '''
        :data dict {
                post_id: int,
                reason: str,
                elaboration: str
            }
        '''
        data = request.data
        post_id = data.get("post_id")
        blog_post = Blog.objects.get(pk=post_id)
        if blog_post is None:
            return Response(
                {
                    "error": f"Blog with ID #{post_id} does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if blog_post.author.user == request.user or request.user.is_superuser:
            return Response(
                {
                    "error": f"You cannot report this post."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        is_reported = ReportedPost.objects.filter(post=blog_post).first()
        if is_reported:
            is_reported.reports += 1
            is_reported.save()
            return Response(
                {
                    "message": f"You have reported this post. Thank you for your feedback."
                },
                status=status.HTTP_200_OK
            )
        elif not is_reported:
            report_dict = {
                "post": blog_post,
                "reporter": request.user,
                "reason": data.get("reason"),
                "elaboration": data.get("elaboration", ""),
                "reports": 1
            }
            serialized = ReportedPostSerializer(data=report_dict)
            if serialized.is_valid():
                serialized.save()
                return Response(
                    serialized.data,
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "error": str(serialized.errors)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )


class TagView(ModelViewSet):
    '''
    Model Viewset for all tags registered in the system:
    '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
