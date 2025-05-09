from django.contrib import admin
from .models import Home
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Home)
class HomePage(SummernoteModelAdmin):

    summernote_fields = ('content',)