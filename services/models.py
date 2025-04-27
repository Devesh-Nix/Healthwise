from django.db import models

class ServiceProvider(models.Model):
    SERVICE_CHOICES = [
        ('nurse', 'Nurse'),
        ('caretaker', 'Caretaker'),
        ('cleaner', 'Cleaner'),
        ('chef', 'Chef'),
        ('other', 'Other')
    ]

    full_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    experience_years = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_service_type_display()})"

class ServiceBooking(models.Model):
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=20)
    address = models.TextField()
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    duration_hours = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking with {self.service_provider.full_name} on {self.date}"
