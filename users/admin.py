from django.contrib import admin
from .models import User


class StudentUser(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'enrollment_date', 'graduation_year', 'address', 'city', 'profile_picture')
admin.site.register(User,StudentUser)

