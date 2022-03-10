from tabnanny import verbose
from django.db import models
from blogapp.model_choices import GENRE_CHOICES
from userapp.models import Author

class Tag(models.Model):
    '''
    Table for hastags used in individual blog posts.
    '''
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Hashtag"
        verbose_name_plural = "Hashtags"


    def __str__(self):
        representation = f"#{self.name}"
        return representation

class Language(models.Model):
    '''
    Table for languages in the blog:
    '''
    name = models.CharField(max_length=32, unique=True)
    titles = models.IntegerField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.name

    @property
    def num_of_titles(self):
        num_blogs = Blog.objects.filter(language__name = self.name).count()
        return num_blogs


class Blog(models.Model):
    '''
    Table for individual blog posts.
    '''
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.DateField(auto_now=True)
    added = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.CharField(max_length=64, choices=GENRE_CHOICES)
    tags = models.ManyToManyField(Tag, related_name='tags')

    class Meta:
        ordering = ['-added']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        representation = f"{self.title} by {self.author.user.username}, - {self.published}"
        return representation

    @property
    def get_author(self):
        return self.author.user.username

    @property
    def get_tags(self):
        tag_list = []
        tags = self.tags.all()
        for tag in tags:
            tag_list.append(tag.name)
        return tag_list

    @property
    def get_summary(self):
        tag_list = []
        tags = self.tags.all()
        for tag in tags:
            tag_list.append(tag.name)
        
        summary = {
            'title': self.title,
            'body': self.body[:100] + '...',
            'genre': self.genre,
            'tags': tag_list
        }
        return summary

    @property
    def absolute_url(self):
        self_url = f"/blog/post/{self.id}"
        return self_url
        
    
