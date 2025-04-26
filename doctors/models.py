from django.db import models
from django.utils.text import slugify

class Doctor(models.Model):
    SPECIALTIES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Dermatology', 'Dermatology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Dentistry', 'Dentistry'),
        ('Psychiatry', 'Psychiatry'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Endocrinology', 'Endocrinology'),
        # Add ALL fields over time... 💥
    ]

    CONSULTATION_TYPES = [
        ('chat', 'Chat'),
        ('video', 'Video Call'),
        ('physical', 'Physical Visit'),
    ]

    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100, choices=SPECIALTIES)
    experience_years = models.IntegerField()
    clinic_address = models.TextField()
    city = models.CharField(max_length=100)
    available_for = models.CharField(max_length=20, choices=CONSULTATION_TYPES)
    phone_number = models.CharField(max_length=15)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name + "-" + self.specialization)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Dr. {self.full_name} ({self.specialization})"
