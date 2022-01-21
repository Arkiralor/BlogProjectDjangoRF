from .models import Author, User
from .serializers import AuthorSerializer, UserSerializer, UserAdminSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token


# Create your views here.

class GetUserView(APIView):
    '''
    Class to GET all model User:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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


class AddUserView(APIView):
    '''
    Register a new user.
    '''

    def post(self, request):
        '''
        POST a new user to the system:
        '''
        data = request.data
        data['password'] = make_password(data.get('password'))
        if 'is_staff' in data.keys():
            data['is_staff'] = False
        if 'is_superuser' in data.keys():
            data['is_superuser'] = False
        deserialized = UserSerializer(data=data)

        if deserialized.is_valid():
            deserialized.save()
            return Response(
                {
                    "success": f"User: {deserialized.data.get('username')} created."
                },
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
    authentication_classes = [TokenAuthentication]
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

        if existing_author is None:
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'


class UserLoginView(APIView):
    '''
    View to login a user and create their token:
    '''

    def post(self, request):
        data = request.data

        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username).first()

        if user is None:
            return Response(
                {
                    "error": "Invalid Username"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not check_password(password, user.password):
            return Response(
                {
                    "error": "Invalid Password"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        token = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": str(token[0])
            },
            status=status.HTTP_202_ACCEPTED
        )


class UserLogoutView(APIView):
    '''
    View to logout user and destroy their token:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = Token.objects.filter(user=request.user).first()
        token.delete()

        return Response(
            {
                "success": "Logged Out."
            }
        )


class SetSuperView(APIView):
    '''
    Class to set superusers:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, id: int):
        try:
            user = User.objects.get(pk=id)
            if user.is_superuser:
                return Response(
                    {
                        "error": "user is already superuser."
                    },
                    status=status.HTTP_200_OK
                )
            user.is_superuser = True
            user.save()
            serialized = UserAdminSerializer(user)
            return Response(
                serialized.data,
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {
                    "error": "User does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )


class SetStaffView(APIView):
    '''
    Class to set superusers:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, id: int):
        try:
            user = User.objects.get(pk=id)
            if user.is_staff:
                return Response(
                    {
                        "error": "user is already staff."
                    },
                    status=status.HTTP_200_OK
                )
            user.is_staff = True
            user.save()
            serialized = UserAdminSerializer(user)
            return Response(
                serialized.data,
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {
                    "error": "User does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )
