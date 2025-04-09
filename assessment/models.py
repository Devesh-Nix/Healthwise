from django.db import models
from patients.models import Patient

class Question(models.Model):
    number = models.PositiveIntegerField(unique=True)
    text = models.TextField()
    
    def __str__(self):
        return f"Q{self.number}: {self.text[:50]}..."
    
class Response(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.BooleanField()
    attempt = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['patient', 'question', 'attempt']

class TestSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    attempt_number = models.PositiveIntegerField()
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['patient', 'attempt_number']
