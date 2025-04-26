from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def book_appointment(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    # patient = get_object_or_404(Patient, user=request.user)

    patients = Patient.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        mode_of_consultation = request.POST.get('mode_of_consultation')

        patient = get_object_or_404(Patient, id=patient_id)

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            mode_of_consultation=mode_of_consultation
        )
        return redirect('appointment_success')

    return render(request, 'book_appointment.html', {'doctor': doctor, 'patients': patients})

@login_required
def appointment_success(request):
    return render(request, 'appointment_success.html')
