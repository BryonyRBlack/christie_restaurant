from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.author = request.user
            contact.post = contact
            contact.save()
            messages.add_message(
                request, messages.SUCCESS,
                'You message has been received, we will be in contact shortly'
            )

    return render(
        request, "contact/contact.html",
        {
            "contact_form":contact_form
        }
    )