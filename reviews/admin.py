from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'rating', 'created_at', 'updated_at')
    search_fields = ('user_username', 'title', 'body')
    list_filter = ('rating', 'created_at')