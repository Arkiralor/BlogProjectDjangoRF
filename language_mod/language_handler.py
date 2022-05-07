import spacy
import en_core_web_sm

class LanguageHAndler:
    '''
    Class to process languages and check similliarity.
    '''

    threshold:float = 0.70
    language:str = "English"

    @classmethod
    def check_if_similiar(cls, query: str, body: str):
        '''
        Function to if query and body are cosine similiar to each other.
        '''
        is_similiar = False
        nlp = spacy.load('en_core_web_sm')
        try:
            doc = nlp(body)
            if nlp(query).similarity(doc) > cls.threshold:
                is_similiar = True
        except Exception as ex:
            print(f"Error: {ex}")
        return is_similiar

