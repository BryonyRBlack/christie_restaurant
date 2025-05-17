from django.shortcuts import render
from .models import Wanted

'''
This pulls the objects created in models and creates a view for them.
It is filited by if the admin has clicked the wanted button.
'''

def wanted_list(request):
    wanted = Wanted.objects.filter(wanted=True)
    return render(
        request,
        "menu/menu.html",
        {
            "wanted": wanted
        }
    )