from django.db import models

from blogapp.models import Blog
from userapp.models import User, Author
from modapp.model_choices import REPORTING_CHOICES

# Create your models here.


class ReportedPost(models.Model):
    reported_post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reason = models.CharField(
        max_length=100, choices=REPORTING_CHOICES, default="spam")
    elaboration = models.TextField(blank=True, null=True)
    reports = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated",)
        unique_together = ("reported_post", "reporter")
        verbose_name = "Reported Post"
        verbose_name_plural = "Reported Posts"
