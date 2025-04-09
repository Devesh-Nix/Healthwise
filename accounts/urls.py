from django.urls import path
from django.contrib.auth import views as auth_views
from .views import clinician_profile ,clinician_signup, ClinicianPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', clinician_profile, name='clinician_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', clinician_signup, name='signup'),
    path('profile/change-password/', ClinicianPasswordChangeView.as_view(), name='change_password'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
