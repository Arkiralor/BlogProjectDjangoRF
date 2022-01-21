from django.db import models
from userapp.models import Author

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        representation = f"#{self.name}"
        return representation


class Blog(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    added = models.DateTimeField(auto_now_add=True)
    GENRE_CHOICES = (
        ('Fiction', 'fiction'),
        ('Non-Fiction', 'non-fiction'),
        ('Poetry', 'poetry'),
        ('Journal', 'journal')
    )
    genre = models.CharField(max_length=64, choices=GENRE_CHOICES)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        representation = f"{self.title} by {self.author.user.username}, - {self.published}"
        return representation
