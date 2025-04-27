from django.db import models

class AmbulanceService(models.Model):
    provider_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    location_city = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.provider_name} ({self.location_city})"

class AmbulanceBooking(models.Model):
    patient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    pickup_address = models.TextField()
    emergency_type = models.CharField(max_length=50, choices=[('normal', 'Normal'), ('critical', 'Critical')])
    booked_at = models.DateTimeField(auto_now_add=True)
    ambulance_service = models.ForeignKey(AmbulanceService, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')  # Pending, Accepted, Completed

    def __str__(self):
        return f"Booking for {self.patient_name} - {self.ambulance_service.provider_name}"
