from django.contrib import admin
from .models import AmbulanceService, AmbulanceBooking

admin.site.register(AmbulanceService)
admin.site.register(AmbulanceBooking)
