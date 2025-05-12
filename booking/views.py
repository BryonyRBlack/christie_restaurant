from django.shortcuts import render
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.

def my_booking(request):
    booking_form = BookingForm()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.author = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking submitted succesfully'
            )

    return render(
        request,
        "booking/booking.html",
        {
            "Booking":Booking,
            "booking_form":booking_form,
        }
    )