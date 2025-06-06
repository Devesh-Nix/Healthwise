from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'clinician', 'dob', 'gender', 'created_at']
    list_filter = ['gender', 'created_at']
    search_fields = ['full_name', 'clinician__username']
