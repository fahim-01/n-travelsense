from django.contrib import admin

# Register your models here.

from .models import Destination,Contact,Booking

admin.site.register(Destination) 
admin.site.register(Contact) 
admin.site.register(Booking) 