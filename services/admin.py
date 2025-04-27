from django.contrib import admin
from .models  import ServiceBooking , ServiceProvider 

admin.site.register(ServiceProvider)
admin.site.register(ServiceBooking)
