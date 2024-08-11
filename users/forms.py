from django import forms
from .models import User, Staff
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['registration_number', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'enrollment_date', 'graduation_year', 'address', 'city', 'profile_picture']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['id_number', 'first_name', 'last_name', 'role', 'email', 'department', 'phone_number', 'profile_picture']

