from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceProvider, ServiceBooking
from django.contrib import messages
from django.core.mail import send_mail

def service_list(request):
    services = ServiceProvider.objects.filter(available=True)
    return render(request, 'service_list.html', {'services': services})

def book_service(request, service_id):
    service_provider = get_object_or_404(ServiceProvider, id=service_id)

    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_phone = request.POST['client_phone']
        address = request.POST['address']
        date = request.POST['date']
        start_time = request.POST['start_time']
        duration_hours = int(request.POST['duration_hours'])

        total_cost = duration_hours * service_provider.hourly_rate

        ServiceBooking.objects.create(
            client_name=client_name,
            client_phone=client_phone,
            address=address,
            service_provider=service_provider,
            date=date,
            start_time=start_time,
            duration_hours=duration_hours,
            total_cost=total_cost
        )
        send_mail(
            subject='Service Booking Confirmation',
            message=f"Dear {ServiceBooking.client_name},\n\nYour booking for {ServiceBooking.service_provider.name} has been confirmed for {ServiceBooking.date} at {ServiceBooking.start_time}.\n\nThank you!",
            from_email='noreply@healthcareplatform.com',
            recipient_list=[ServiceBooking.client_email],
            fail_silently=False,
        )


        messages.success(request, "✅ Service booked successfully!")
        return redirect('service_list')

    return render(request, 'book_service.html', {'service_provider': service_provider})
