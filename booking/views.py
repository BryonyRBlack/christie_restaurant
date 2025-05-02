from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm

# Create your views here.
def my_booking(request):
    booking_form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {
            "Booking":Booking,
            "booking_form":booking_form,
        }
    )