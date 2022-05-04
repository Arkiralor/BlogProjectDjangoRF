from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from modapp.models import ReportedPost
from modapp.serializers import ReportedPostSerializer
from auth.custom_permissions import IsModerator
# Create your views here.


class GetAllReportedView(APIView):
    '''
    View to GET all reported posts:
    '''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsModerator,)

    def get(self, request):
        '''
        GET all reported posts:
        '''
        queryset = ReportedPost.objects.all()
        serialized = ReportedPostSerializer(queryset, many=True)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )
