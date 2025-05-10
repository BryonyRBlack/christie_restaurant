from django.contrib import admin
from .models import Category, Food

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'available',
    ]
    prepopulated_fields = {'slug': ('name',)}