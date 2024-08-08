from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['registration_number', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'enrollment_date', 'graduation_year', 'address', 'city', 'profile_picture']