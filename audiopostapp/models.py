from django.db import models

from userapp.models import Author
from audiopostapp.model_choices import GENRE_CHOICES

# Create your models here.

class AudioTag(models.Model):
    '''
    Table for hastags used in individual blog posts.
    '''
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Audio Hashtag"
        verbose_name_plural = "Audio Hashtags"

    def __str__(self):
        representation = f"#{self.name}"
        return representation


class AudioLanguage(models.Model):
    '''
    Table for languages in the blog:
    '''
    name = models.CharField(max_length=32, unique=True)
    titles = models.IntegerField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Audio Language"
        verbose_name_plural = "Audio Languages"

    def __str__(self):
        return self.name

    @property
    def num_of_titles(self):
        self.titles = AudioPost.objects.filter(language__name = self.name).count()
        self.save()
        return self.titles

class AudioPost(models.Model):
    name = models.CharField(max_length=64)
    audio = models.FileField(upload_to='media/audioposts/audiodiles/', blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='recorded_by')
    language = models.ForeignKey(
        AudioLanguage, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name="written_in"
        )
    genre = models.CharField(max_length=64, choices=GENRE_CHOICES)
    tags = models.ManyToManyField(AudioTag, related_name='tags')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-added']
        verbose_name = 'Audio Post'
        verbose_name_plural = 'Audio Posts'


    def __str__(self):
        representation = f"{self.title} by {self.author.user.username}, - {self.published}"
        return representation
