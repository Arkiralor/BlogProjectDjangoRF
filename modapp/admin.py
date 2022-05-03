from django.contrib import admin
from modapp.models import ReportedPost
# Register your models here.

@admin.register(ReportedPost)
class ReportedPostAdmin(admin.ModelAdmin):
    raw_id_fields = ('reported_post',)
    link_fields = ('reported_post',)
    list_display = ('reported_post', 'reporter')
    search_fields = ('reported_post__title', 'reported_post__body', 'reporter__username')
