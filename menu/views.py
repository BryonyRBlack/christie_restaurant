from django.shortcuts import get_object_or_404, render
from .models import Category, Food
# Create your views here.

def food_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    food = Food.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        food = food.filter(category=category)
    return render(
        request,
        'menu/menu.html'
    )