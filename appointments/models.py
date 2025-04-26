from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    CONSULTATION_MODES = [
        ('chat', 'Chat'),
        ('video', 'Video Call'),
        ('physical', 'Physical Visit'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    mode_of_consultation = models.CharField(max_length=10, choices=CONSULTATION_MODES)
    created_at = models.DateTimeField(auto_now_add=True)

    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment: {self.patient.full_name} with Dr. {self.doctor.full_name} on {self.appointment_date}"
