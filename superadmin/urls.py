from django.urls import path
from .views import superadmin_dashboard

urlpatterns = [
    path('Sad/dashboard/', superadmin_dashboard, name='superadmin_dashboard'),
]
