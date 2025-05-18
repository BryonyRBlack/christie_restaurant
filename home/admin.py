from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Home


'''
This registers the Home model to the admin page so that it can be accessed.
This uses Summernote for ease of typing.
'''


# Register your models here.
@admin.register(Home)
class HomePage(SummernoteModelAdmin):

    summernote_fields = ("content",)
