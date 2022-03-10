from blogapp.models import Blog, Tag, Language
from typing import List
from blogapp.model_choices import LANG_DICT


import spacy
from spacy_langdetect import LanguageDetector
from spacy.language import Language as ln
from spacy_langdetect import LanguageDetector
import en_core_web_sm


class TagUtils:
    '''
    Class to handle hashtags in blogposts while adding a new blog-post:
    '''

    def __init__(self, input_list: List[str]):
        '''
        Initialization method for the class:
        '''

        # Reinitializing these so that the previously passed list is erased,
        # since the __init__ method is being called on the same class-object
        # in the calling function, using a loop.
        self.TAG_LIST: List[str] = []
        self.ID_LIST: List[int] = []
        for item in input_list:
            self.TAG_LIST.append(item.replace("#", ""))

    def __repr__(self):
        '''
        Representation method for the class:
        '''
        return f"{self.TAG_LIST}"

    def resolve_tags(self):
        '''
        Method to check if the passed tags exist in the database table:
        If they exist, return their IDs.
        If they do not exist, add them to the library and return their IDs.
        '''
        for item in self.TAG_LIST:
            tag = Tag.objects.filter(name=item).first()
            if not tag:
                new_tag = Tag(name=item)
                new_tag.save()
                self.ID_LIST.append(new_tag.id)
            elif tag:
                self.ID_LIST.append(tag.id)
        return self.ID_LIST


class LanguageUtils:
    '''
    Class to handle language detection in blogposts while adding a new blog-post:
    '''

    def __init__(self, input_text: str):
        '''
        Initialization method for the class:
        '''
        self.input_text = input_text

    def __repr__(self):
        '''
        Representation method for the class:
        '''
        return f"{self.input_text}"

    def detect_language(self):
        '''
        Method to detect the language of the passed text:
        '''
        ln.factory("language_detector", func=create_lang_detector)
        nlp = en_core_web_sm.load(disable=[None])
        nlp.max_length = 2000000

        nlp.add_pipe("language_detector", last=True)

        doc = nlp(self.input_text)
        lang_code = doc._.language.get("language")
        print(doc._.language)

        return LANG_DICT.get(lang_code)

    def enter_language(self, name: str):
        language = Language.objects.filter(name=name).first()
        code_id = None
        if language is not None:
            code_id = language.id
        else:
            new_lang = Language(name=name)
            new_lang.save()
            code_id = new_lang.id
        return code_id


@ln.factory('language_detector')
def create_lang_detector(nlp, name):
    '''
    function to create language model.
    '''
    return LanguageDetector()


if __name__ == "__main__":
    pass
