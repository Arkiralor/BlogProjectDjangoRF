import spacy
from blogapp.models import Blog
from blogapp.serializers import BlogOutSerializer, LanguageSerializer
import en_core_web_sm

class LanguageHAndler:
    '''
    Class to process languages and recommend posts with similliar context.
    '''

    threshold:float = 0.70
    language:str = "English"

    @classmethod
    def search_similiar(cls, query: str, language: str):
        '''
        Function to look for posts who are cosine similiar to the passed query.
        '''
        nlp = spacy.load('en_core_web_sm')
        if language is None:
            language = cls.language
        posts = Blog.objects.filter(language__name=language)
        serialized = BlogOutSerializer(posts, many=True)
        recommended_posts = []
        for post in serialized.data:
            doc = nlp(post.get("body", ""))
            if nlp(query).similarity(doc) > cls.threshold:
                recommended_posts.append(post)
        return recommended_posts

