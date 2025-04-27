from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.mail import send_mail

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

        # After saving appointment
        send_mail(
            subject='Appointment Confirmed',
            message=f"Dear {Appointment.patient.full_name},\n\nYour appointment with Dr. {Appointment.doctor.clinician_profile.full_name} has been confirmed for {Appointment.date} at {Appointment.time}.\n\nThank you!",
            from_email='noreply@healthcareplatform.com',
            recipient_list=[Appointment.patient.email],
            fail_silently=False,
        )

        send_mail(
            subject='New Appointment Booked',
            message=f"Dear Dr. {Appointment.doctor.clinician_profile.full_name},\n\nA new appointment has been booked with patient {Appointment.patient.full_name} on {Appointment.date} at {Appointment.time}.\n\nPlease be ready!",
            from_email='noreply@healthcareplatform.com',
            recipient_list=[Appointment.doctor.email],
            fail_silently=False,
        )

        return redirect('appointment_success')

    return render(request, 'book_appointment.html', {'doctor': doctor, 'patients': patients})

@login_required
def appointment_success(request):
    return render(request, 'appointment_success.html')


@login_required
def patient_appointments(request):
    # Get clinician's patients
    from patients.models import Patient
    try:
        patient = Patient.objects.get(id=request.GET.get('patient_id'))
    except Patient.DoesNotExist:
        patient = None

    if not patient:
        return redirect('clinician_dashboard')
    
    appointments = Appointment.objects.filter(patient=patient).order_by('appointment_date', 'appointment_time')

    return render(request, 'patient_appointments.html', {
        'patient': patient,
        'appointments': appointments
    })

@login_required
def doctor_appointments(request, doctor_slug):
    from doctors.models import Doctor  # import here to avoid circular
    try:
        # doctor = Doctor.objects.get(slug=request.GET.get('doctor_slug'))
        doctor = get_object_or_404(Doctor, slug=doctor_slug)
    except Doctor.DoesNotExist:
        doctor = None

    if not doctor:
        return redirect('clinician_dashboard')

    appointments = Appointment.objects.filter(doctor=doctor).order_by('appointment_date', 'appointment_time')
    
    return render(request, 'doctor_appointments.html', {
        'doctor': doctor,
        'appointments': appointments
    })
