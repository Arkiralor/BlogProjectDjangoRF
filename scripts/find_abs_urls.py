from blogapp.models import Blog


def main():
    posts = Blog.objects.all()

    url_list = list()

    for post in posts:
        url_list.append(post.absolute_url)

    print(url_list)
