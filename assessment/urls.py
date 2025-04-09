from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('take-test/<int:patient_id>/', views.take_test, name='take_test'),
    path('submitted/', lambda request: render(request, 'test_submitted.html'), name='test_submitted'),
    # path('report/<int:patient_id>/', views.generate_report_attempt, name='generate_report'),
    path('report/<int:patient_id>/attempt/<int:attempt>/', views.generate_report_attempt, name='generate_report_attempt'),
    # path('patient/<int:patient_id>/attempts/', views.patient_attempts, name='patient_attempts'),


    # path('report/<int:patient_id>/attempt/<int:attempt_number>/', views.generate_report_attempt, name='generate_report_attempt'),
    path('patient/<int:patient_id>/attempts/', views.patient_attempts, name='patient_attempts'),
    path('adminpanel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('upload-questions/', views.bulk_upload_questions, name='bulk_upload_questions'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('select-test/', views.select_test, name='select_test'),
    # path('patients/<int:patient_id>/take-test/', views.take_test, name='take_test'),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)