from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ClinicianSignupForm
from .models import ClinicianProfile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ClinicianProfile
from .forms import ClinicianProfileForm



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

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class ClinicianPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'profile/change_password.html'
    success_url = reverse_lazy('clinician_profile')
    success_message = "✅ Your password was changed successfully."