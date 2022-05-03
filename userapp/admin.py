from django.contrib import admin
from .models import User, Author


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser', 'has_key', 'user_type')
    list_filter = ('is_staff', 'is_superuser', 'user_type')
    search_fields = ('username', 'email', 'user_type')
    list_per_page = 10


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_joined')
    raw_id_fields = ('user',)
    link_fields = ('user__username',)
    search_fields = ('user__username', 'user__email',
                     'user__is_staff', 'user__is_superuser','user__user_type', 'user__has_key')
    list_per_page = 10
