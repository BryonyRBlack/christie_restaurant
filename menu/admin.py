from django.contrib import admin
from .models import Wanted

# Register your models here.
@admin.register(Wanted)
class WantedAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'available',
    ]