from django.shortcuts import render, redirect, get_object_or_404
from .models import AmbulanceService, AmbulanceBooking
from django.contrib import messages
from django.core.mail import send_mail

def ambulance_services_list(request):
    ambulances = AmbulanceService.objects.filter(available=True)
    return render(request, 'ambulance_list.html', {'ambulances': ambulances})

def book_ambulance(request, ambulance_id):
    ambulance = get_object_or_404(AmbulanceService, id=ambulance_id)

    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        phone = request.POST['phone']
        pickup_address = request.POST['pickup_address']
        emergency_type = request.POST['emergency_type']

        AmbulanceBooking.objects.create(
            patient_name=patient_name,
            phone=phone,
            pickup_address=pickup_address,
            emergency_type=emergency_type,
            ambulance_service=ambulance,
        )
        messages.success(request, "✅ Ambulance booked successfully! Help is on the way.")
        send_mail(
            subject='Ambulance Booking Confirmation',
            message=f"Dear {AmbulanceBooking.patient_name},\n\nYour ambulance has been booked successfully. Pickup Location: {AmbulanceBooking.pickup_address}. Emergency Type: {AmbulanceBooking.emergency_type}.\n\nHelp is on the way!",
            from_email='noreply@healthcareplatform.com',
            recipient_list=[request.user.email],
            fail_silently=False,
            )

        return redirect('ambulance_services')

    return render(request, 'book_ambulance.html', {'ambulance': ambulance})
