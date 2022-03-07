from django.contrib import admin
from .models import User, Author


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_per_page = 10


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_joined')
    raw_id_fields = ('user',)
    link_fields = ('user',)
    list_filter = ('date_joined',)
    search_fields = ('user__username', 'user__email',
                     'user__is_staff', 'user__is_superuser')
    list_per_page = 10
