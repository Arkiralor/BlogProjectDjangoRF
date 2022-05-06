from django.test import TestCase
from blogapp.utils import LanguageUtils

# Create your tests here.

class TestBlogApp(TestCase):
    '''
    Test cases for BlogApp.
    '''

    def test_detect_language(self):
        '''
        Test if a language is detected correctly, eg: English
        '''
        query = "Hello and welcome to this wonderful, wonderful world."
        language = LanguageUtils(query).detect_language()
        self.assertEqual(language, "English")

    def test_unknown_language(self):
        '''
        Test if an unknown language is detected correctly.
        '''
        query = "Moi aaji janu eyaat ki kori aasu?"
        language = LanguageUtils(query).detect_language()
        assert(language != "English")


