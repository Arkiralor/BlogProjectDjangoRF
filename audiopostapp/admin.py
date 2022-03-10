from django.contrib import admin
from audiopostapp.models import AudioLanguage, AudioPost, AudioTag

# Register your models here.

@admin.register(AudioLanguage)
class AudioLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'titles')
    search_fields = ('name',)

@admin.register(AudioPost)
class AudioPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'genre', 'added')
    list_filter = ('author', 'genre')
    raw_id_fields = ('author', 'language', 'tags')
    search_fields = ('name', 'author__user__username')

@admin.register(AudioTag)
class AudioTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)