from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    contact_form = ContactForm()
    return render(
        request, "contact/contact.html",
        {
            "contact_form":contact_form
        }
    )