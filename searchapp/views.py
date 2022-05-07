from blogapp.models import Blog, Tag, Language
from blogapp.serializers import BlogOutSerializer, TagSerializer, LanguageSerializer
from searchapp.utils import SearchUtil

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class SearchPostView(APIView):
    '''
    API to search for a particular blog post.
    '''
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        '''
        :params dict:
        query:str = None
        type:str = TITLE|BODY|ALIKE 
        '''
        query = request.GET.get('query')
        type = request.GET.get('type')
        search_util = SearchUtil(query, type)
        resp = search_util.resolve()
        if resp.get("results") is None or len(resp.get("results")) == 0:
            return Response(
                {
                    "error": f"No results found for query: {query} and type: {type}"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            resp,
            status=status.HTTP_200_OK
        )
