from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Category, Food
# Create your views here.

class FoodList(generic.ListView):
    queryset = Food.objects.filter(available=True)
    template_name = "menu/html"

def food_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Food.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        'menu/menu.html',
        {
            'category': category,
            'categories': categories,
            'products': products
        }
    )