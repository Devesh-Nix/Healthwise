from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login
from .forms import ClinicianProfileForm, ClinicianSignupForm, PatientSignupForm
from .models import ClinicianProfile, PatientProfile
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

User = get_user_model()

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            PatientProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, "✅ Registered and Logged in Successfully.")
            return redirect('patient_dashboard')
    else:
        form = PatientSignupForm()
    return render(request, 'patient_signup.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "✅ Logged in Successfully.")
            return redirect('patient_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'patient_login.html', {'form': form})




def clinician_signup(request):
    if request.method == 'POST':
        form = ClinicianSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            ClinicianProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                specialization=form.cleaned_data['specialization'],
                clinic_name=form.cleaned_data.get('clinic_name', ''),
                phone_number=form.cleaned_data.get('phone_number', '')
            )
            login(request, user)
            return redirect('clinician_dashboard')
    else:
        form = ClinicianSignupForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def clinician_profile(request):
    profile, created = ClinicianProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ClinicianProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('clinician_profile')
    else:
        form = ClinicianProfileForm(instance=profile)

    return render(request, 'clinician_profile.html', {'form': form})


class ClinicianPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('clinician_profile')
    success_message = "✅ Your password was changed successfully."


def landing_page(request):
    return render(request, 'landing_base.html')