from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'booking_date', 'num_people', 'special_requests',)