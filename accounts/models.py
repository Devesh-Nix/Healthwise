from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    is_clinician = models.BooleanField(default=True)  # Extend later for roles


class ClinicianProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    clinic_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return self.full_name
