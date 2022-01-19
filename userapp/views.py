from distutils import errors
from django.shortcuts import render
from .models import Author, User
from .serializers import AuthorSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.

class UserView(APIView):
    '''
    Class to GET/POST model User:
    '''
    
    def get(self, request):
        '''
        GET a list of all users in system:
        '''
        if request.user.is_staff:
            queryset = User.objects.all()

            serialized = UserSerializer(queryset, many=True)

            return Response(
                serialized.data,
                status=status.HTTP_302_FOUND
            )
        else:
            return Response(
                {
                    "error": "Unauthorized"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

    def post(self, request):
        '''
        POST a new user to the system:
        '''
        data = request.data
        data['password'] = make_password(data.get('password'))

        deserialized = UserSerializer(data=data)

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

class GenerateAuthorView(APIView):
    '''
    Class to GET/POST Authors generated from users:
    '''
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        GET a list of all generated authors in the system:
        '''
        if request.user.is_staff:
            queryset = Author.objects.all()
            serialized = AuthorSerializer(queryset, many=True)

            return Response(
                serialized.data,
                status=status.HTTP_302_FOUND
            )
        else:
            return Response(
                {
                    "error": "Unauthorized"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

    def post(self, request):
        '''
        POST/Generate a new author/profile from an existing user in the system:
        '''
        existing_author = Author.objects.filter(user=request.user).first()

        if not existing_author:
            author = Author(user=request.user)
            author.save()
            serialized = AuthorSerializer(author)
            return Response(
                {
                    "success": f"Author: {serialized.data} created for User: {request.user}."
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "error": f"Author already generated for User: {request.user}."
                },
                status=status.HTTP_201_CREATED
            )




class AuthorView(ModelViewSet):
    '''
    Model Viewset for the model/table 'Author':
    '''
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'
