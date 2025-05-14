from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'num_people', 'booking_date', 'special_requests',)
        
