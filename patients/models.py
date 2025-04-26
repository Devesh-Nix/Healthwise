from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()


class Patient(models.Model):
    clinician = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class PatientHistory(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='histories')
    date_recorded = models.DateField(auto_now_add=True)
    condition_title = models.CharField(max_length=255)
    description = models.TextField()
    prescribed_treatment = models.TextField(blank=True, null=True)
    diagnosed_by = models.CharField(max_length=255, blank=True, null=True)  # Doctor name (optional)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.condition_title}"