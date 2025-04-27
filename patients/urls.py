from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', clinician_dashboard, name='clinician_dashboard'),
    path('patient/<int:patient_id>/add-history/', add_patient_history, name='add_patient_history'),
    path('patient/<int:patient_id>/', patient_detail, name='patient_detail'),
    path('dashboard/', patient_dashboard, name='patient_dashboard'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)