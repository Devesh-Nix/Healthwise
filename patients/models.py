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
