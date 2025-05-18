from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

'''
This allows the contact form to be present on the page.
It checks the form is valid
and confirms to the user that the message has been sent.
'''


def contact_us(request):

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.author = request.user
            contact.post = contact
            contact.save()
            messages.add_message(
                request, messages.SUCCESS,
                "You message has been received, we will be in contact shortly"
            )

    contact_form = ContactForm()

    return render(
        request, "contact/contact.html",
        {
            "contact_form": contact_form
        }
    )
