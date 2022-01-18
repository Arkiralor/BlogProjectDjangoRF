from distutils import errors
from django.shortcuts import render
from .models import Author, User
from .serializers import AuthorSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

# Create your views here.

class UserView(APIView):
    
    def get(self, request):
        queryset = User.objects.all()

        serialized = UserSerializer(queryset, many=True)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )

    def post(self, request):
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


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'
