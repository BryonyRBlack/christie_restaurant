from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)