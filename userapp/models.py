from django.db import models
from django.contrib.auth.models import AbstractUser
from userapp.model_choices import USER_TYPE_CHOICES

# Create your models here.


class User(AbstractUser):
    """
    Custom user model.
    """
    has_key = models.BooleanField(default=False)
    user_type = models.CharField(
        max_length=32,
        choices=USER_TYPE_CHOICES,
        default='normal_user',
        blank=True,
        null=True
    )
    


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    @property
    def username(self):
        return self.user.username

    @property
    def user_id(self):
        return self.user.id

    @property
    def get_function(self):
        user_id = self.user.id
        username = self.user.username
        is_staff = self.user.is_staff
        is_superuser = self.user.is_superuser
        rep_dict = {
            'id': user_id,
            'username': username,
            'function': {
                'is_staff': is_staff,
                'is_superuser': is_superuser
            }
        }
        return rep_dict
