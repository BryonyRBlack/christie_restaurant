from django.shortcuts import render
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.views import generic

# Create your views here.

class CreateView(generic.edit.CreateView):
    model = Booking
    fields = ['user', 'num_people']
    template_name = 'booking/booking.html'
    def my_booking(self):
        form = super().get_form()
        form.fields["Select a Date"].widget = DatePickerInput()
        return form
    
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