from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user_username', 'title', 'message')
    list_filter = ('created_at',)