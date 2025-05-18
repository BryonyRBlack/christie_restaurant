from django.shortcuts import render
from .models import Home


'''
This pulls the Home objets to ensure that they are loaded to the page.
'''


def home_page(request):
    home = Home.objects.all().order_by("-title").first()

    return render(
        request, "home/index.html", {"home": home}
    )
