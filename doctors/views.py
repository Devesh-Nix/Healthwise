from django.shortcuts import render
from .models import Doctor
from django.db.models import Q
from django.shortcuts import get_object_or_404

def doctor_list(request):
    doctors = Doctor.objects.all()

    query = request.GET.get('q')
    if query:
        doctors = doctors.filter(
            Q(full_name__icontains=query) |
            Q(specialization__icontains=query) |
            Q(city__icontains=query)
        )

    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_detail(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    return render(request, 'doctor_detail.html', {'doctor': doctor})
