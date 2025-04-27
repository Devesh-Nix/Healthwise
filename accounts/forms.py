from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *

User = get_user_model()

class PatientSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_patient = True
        if commit:
            user.save()
            from .models import PatientProfile
            PatientProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address']
            )
        return user


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
