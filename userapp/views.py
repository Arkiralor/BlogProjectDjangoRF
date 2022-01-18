from django.shortcuts import render
from .models import Author, User
from .serializers import AuthorSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'
