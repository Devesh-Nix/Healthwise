from django.db import models

class Report(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    summary = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)
