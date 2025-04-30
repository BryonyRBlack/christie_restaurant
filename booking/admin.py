from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_date', 'num_people', 'created_at')
    search_fields = ('user_username', 'special_requests')
    list_filter = ('booking_date',)