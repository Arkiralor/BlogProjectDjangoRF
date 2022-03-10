from blogapp.models import Blog, Language

def main():
    english = Language.objects.filter(name='English').first()

    posts = Blog.objects.all()
    for post in posts:
        post.language = english
        post.save()

if __name__=="__main__":
    main()