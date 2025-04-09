from django.urls import path
from .views import clinician_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', clinician_dashboard, name='clinician_dashboard'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)