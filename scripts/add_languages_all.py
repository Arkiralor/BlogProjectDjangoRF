from blogapp.models import Blog, Language
from blogapp.utils import LanguageUtils

def main():
    posts = Blog.objects.all()
    for bpost in posts:
        lang_util = LanguageUtils(input_text=bpost.body)
        
        if bpost.language is None:            
            lang = lang_util.detect_language()
            lang_obj = Language.objects.filter(name=lang).first()
            
            try:
                if lang_obj is not None:
                    bpost.language = lang_obj
                    bpost.save()
                else:
                    new_lang = Language(name=lang)
                    new_lang.save()
                    bpost.language = new_lang
                    bpost.save() 
            except Exception as ex:
                print(f"Error: {ex} for post: {bpost.id}. {bpost.title}")
        
        else:
            pass 

if __name__=="__main__":
    main()