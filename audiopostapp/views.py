from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from userapp.models import Author, User
from userapp.serializers import AuthorSerializer
from audiopostapp.models import AudioPost, AudioTag, AudioLanguage
from audiopostapp.serializers import AudioPostSerializer, AudioTagSerializer, AudioLanguageSerializer

# Create your views here.

class AudioPostView(APIView):
    '''
    View to GET all audio-posts
    '''

    def get(self, request):
        '''
        GET all audio-posts:
        '''
        queryset = AudioPost.objects.all()
        serialized = AudioPostSerializer(queryset, many=True)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )
