from django.urls import path
from . import views

urlpatterns = [
    path('book/<slug:slug>/', views.book_appointment, name='book_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
    path('patient/<int:patient_id>/', views.patient_appointments, name='patient_appointments'),
    path('doctor/<slug:doctor_slug>/', views.doctor_appointments, name='doctor_appointments'),
]
