from django.db import models
from userapp.models import Author

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    added = models.DateTimeField(auto_now_add=True)

    CATEGORY_CHOICES = (
        ('#fiction', 'fiction'),
        ('#non-fiction', 'non-fiction'),
        ('#journal', 'journal'),
        ('#poetry', 'poetry'),
        ('#article', 'article'),
        ('#opinion-piece', 'opinion-piece'),
        ('#tech', 'tech')
    )
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)

    def __str__(self):
        representation = f"{self.title} by {self.author.user.username}, - {self.published}"
        return representation
