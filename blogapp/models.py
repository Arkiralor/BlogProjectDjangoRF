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


class Blog(models.Model):
    '''
    Table for individual blog posts.
    '''
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    added = models.DateTimeField(auto_now_add=True)
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
    def get_summary(self):
        tag_list = []
        title = self.title
        body = self.body[:100]
        genre = self.genre
        tags = self.tags.all()
        for tag in tags:
            tag_list.append(tag.name)
        
        summary = {
            'title': title,
            'body': body,
            'genre': genre,
            'tags': tag_list
        }
        return summary

    @property
    def absolute_url(self):
        self_url = f"/blog/post/{self.id}"
        return self_url
        
    
