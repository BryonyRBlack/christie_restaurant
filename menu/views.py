from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Wanted
# Create your views here.

class WantedList(generic.ListView):
    queryset = Wanted.objects.filter(available=True)
    template_name = "menu/html"

def wanted_list(request):
    wanted = Wanted.objects.filter(available=True)
    return render(
        request,
        'menu/menu.html',
        {
            'wanted': wanted
        }
    )