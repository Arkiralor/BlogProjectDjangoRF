from django.contrib import admin
from .models import Blog, Language, Tag

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'added')
    list_filter = ('published', 'author')
    raw_id_fields = ('author', 'tags', 'language')
    search_fields = ('title', 'body', 'author__user__username')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
