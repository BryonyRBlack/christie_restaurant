from .models import Contact
from django import forms

'''
This form allows users to get in touch. 
It does not require the user to be logged in.
'''

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")