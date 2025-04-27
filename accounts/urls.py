from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', clinician_profile, name='clinician_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', clinician_signup, name='signup'),
    path('profile/change-password/', ClinicianPasswordChangeView.as_view(), name='change_password'),
    path('patient/signup/', patient_signup, name='patient_signup'),
    path('patient/login/', patient_login, name='patient_login'),
    path('patient/logout/', LogoutView.as_view(next_page='patient_login'), name='patient_logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
