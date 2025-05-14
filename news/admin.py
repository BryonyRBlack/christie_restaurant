from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published']
    list_filter = ['published', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}