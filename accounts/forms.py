from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ClinicianProfile

class ClinicianSignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")
    specialization = forms.CharField(max_length=100, required=True)
    clinic_name = forms.CharField(max_length=150, required=False, label="Clinic/Hospital Name")
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'specialization', 'clinic_name', 'phone_number', 'password1', 'password2')


class ClinicianProfileForm(forms.ModelForm):
    class Meta:
        model = ClinicianProfile
        fields = ['full_name', 'specialization', 'clinic_name', 'phone_number', 'profile_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'clinic_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
