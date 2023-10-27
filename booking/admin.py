from django.contrib import admin
from .models import Booking, userProfile
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import messages


@admin.register(Booking)
class BookingComments(SummernoteModelAdmin):

    list_filter = ('status', 'created_on', 'booking_date')
    readonly_fields = ('booking_id',)
    summernote_fields = ('booking_comments')
    list_display = (
        'booking_id', 'user', 'booking_date', 'booking_time', 'guest_num',
        'status')
    search_fields = ('user',)
    actions = ['accept_booking', 'cancel_booking']

    def accept_booking(self, request, queryset):
        queryset.update(status=1)
        self.message_user(request, 'Selected bookings have been accepted.')

    def cancel_booking(self, request, queryset):
        queryset.update(status=2)
        self.message_user(request, 'Selected bookins have been cancelled.')

    accept_booking.short_description = 'Accept selected bookings'
    cancel_booking.short_description = 'Cancel selected bookings'


@admin.register(userProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    search_fields = ('user', 'last_name', 'phone_number')




