from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Article)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'published')
    list_filter = ['published', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

admin.site.register(Comment)