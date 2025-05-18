from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact


'''
This registers the contact form to the admin site,
so that sent messages can be read by those with access.
Summernote is included for ease.
Filters are also used.
'''


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message")
    list_filter = ("created_at",)
