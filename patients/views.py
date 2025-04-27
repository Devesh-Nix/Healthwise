from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .models import Patient




@login_required
def clinician_dashboard(request):
    patients = Patient.objects.filter(clinician=request.user)
    return render(request, 'clinician_dashboard.html', {'patients': patients})

@login_required
def add_patient(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST.get('email', '')

        Patient.objects.create(
            clinician=request.user,
            full_name=full_name,
            dob=dob,
            gender=gender,
            email=email
        )
        messages.success(request, "Patient added successfully.")
        return redirect('add_patient')

    return render(request, 'add_patient.html')

@login_required
def select_test(request):
    patients = Patient.objects.filter(clinician=request.user)

    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        test_name = request.POST['test_name']

        if test_name == "MCMI-III":
            return redirect('take_test', patient_id=patient_id)

        messages.warning(request, "This test is not available yet.")
        return redirect('select_test')

    return render(request, 'select_test.html', {"patients": patients})

from .models import PatientHistory

@login_required
def add_patient_history(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        condition_title = request.POST.get('condition_title')
        description = request.POST.get('description')
        prescribed_treatment = request.POST.get('prescribed_treatment')
        diagnosed_by = request.POST.get('diagnosed_by')

        PatientHistory.objects.create(
            patient=patient,
            condition_title=condition_title,
            description=description,
            prescribed_treatment=prescribed_treatment,
            diagnosed_by=diagnosed_by
        )
        return redirect('patient_detail', patient_id=patient.id)

    return render(request, 'add_history.html', {'patient': patient})

@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    histories = patient.histories.all().order_by('-date_recorded')  # Latest first

    return render(request, 'patient_detail.html', {
        'patient': patient,
        'histories': histories,
    })

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')