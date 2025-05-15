from .models import Review
from django import forms

class ReviewForms(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user', 'message',)