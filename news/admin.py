from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin

'''
This registers the Article model to the admin page.
Summernote is included to make writing on the admin page easier.
Prepopulated fields allow ensurance that the title and the slug are the same
The admin user is able to filter through the article objects
'''

# Register your models here.
@admin.register(Article)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "published")
    list_filter = ["published", "title"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("body",)

admin.site.register(Comment)