from django.shortcuts import render
from django.views import generic
from .models import Home

# Create your views here.
#class home(generic.ListView):
    #queryset = Home.objects.all()
    #template_name = "home/index.html"

def home_page(request):
    home = Home.objects.all().order_by('-title').first()

    return render(
        request, "home/index.html", {"home": home}
    )