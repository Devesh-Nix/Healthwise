from django.shortcuts import render
from appointments.models import Appointment
from ambulance.models import AmbulanceBooking
from medicines.models import MedicineOrder
from services.models import ServiceBooking
from patients.models import Patient
from doctors.models import Doctor

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def superadmin_dashboard(request):
    doctor_count = Doctor.objects.count()
    patient_count = Patient.objects.count()
    appointment_count = Appointment.objects.count()
    ambulance_count = AmbulanceBooking.objects.count()
    medicine_orders = MedicineOrder.objects.count()
    service_bookings = ServiceBooking.objects.count()

    context = {
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'appointment_count': appointment_count,
        'ambulance_count': ambulance_count,
        'medicine_orders': medicine_orders,
        'service_bookings': service_bookings
    }
    latest_appointments = Appointment.objects.order_by('-created_at')[:5]
    latest_ambulances = AmbulanceBooking.objects.order_by('-booked_at')[:5]
    latest_medicines = MedicineOrder.objects.order_by('-ordered_at')[:5]
    latest_services = ServiceBooking.objects.order_by('-booked_at')[:5]

    context.update({
        'latest_appointments': latest_appointments,
        'latest_ambulances': latest_ambulances,
        'latest_medicines': latest_medicines,
        'latest_services': latest_services,
    })

    return render(request, 'superadmin_dashboard.html', context)
