from django.contrib import admin
from .models import Wanted


'''
Wanted list is registered to the admin page here
This is only available to those with access to the admin page
'''


# Register your models here.
@admin.register(Wanted)
class WantedAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "wanted",
    ]
