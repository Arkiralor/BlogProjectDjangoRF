from blogapp.models import Blog
from blogapp.serializers import BlogOutSerializer
from blogapp.utils import LanguageUtils
from language_mod.language_handler import LanguageHAndler


class SearchUtil:
    '''
    Class to handle blog searches
    '''

    def __init__(self, query: str = None, type: str = None):
        self.query = query
        self.type = type

    def resolve(self):
        '''
        Resolve the search query to call the appropriate method and return the results.
        '''
        if self.query is None or (self.type is None or self.type not in ["TITLE", "BODY", "ALIKE"]):
            raise Exception("Invalid Request")

        if self.type == "TITLE":
            posts = self.search_title()
        elif self.type == "BODY":
            posts = self.search_body()
        elif self.type == "ALIKE":
            posts = self.search_alike()

        return posts

    def search_title(self):
        '''
        Search by title.
        '''
        posts = Blog.objects.filter(title__icontains=self.query)
        serialized = BlogOutSerializer(posts, many=True)
        resp = {
            "results": serialized.data,
            "query": self.query,
            "length": len(serialized.data),
        }
        return resp

    def search_body(self):
        '''
        Search by body.
        '''
        posts = Blog.objects.filter(body__icontains=self.query)
        serialized = BlogOutSerializer(posts, many=True)
        resp = {
            "results": serialized.data,
            "query": self.query,
            "length": len(serialized.data),
        }
        return resp

    def search_alike(self):
        '''
        Search by similliarity of body content.
        '''
        language = LanguageUtils(query).detect_language()
        if language is None or language == "Unknown":
            raise Exception("Language not detected")
        if language != "English":
            raise Exception(
                "Currently, only English recommendations are supported")

        query = self.query

        resp = {
            "results": [],
            "query": query,
        }

        posts = Blog.objects.filter(language=language)
        serialized = BlogOutSerializer(posts, many=True)
        for item in serialized.data:
            if LanguageHAndler.check_if_similiar(query, item.get("body", "")):
                resp["results"].append(item)
        resp["lenght"] = len(resp["results"])
        if resp.get("results") is None or resp["lenght"] == 0:
            raise Exception("No results found")
        return resp
