from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Patient

@login_required
def clinician_dashboard(request):
    patients = Patient.objects.filter(clinician=request.user)
    return render(request, 'clinician_dashboard.html', {'patients': patients})
