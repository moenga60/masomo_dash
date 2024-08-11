from django.contrib import admin
from .models import User, Staff


class StudentUser(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'enrollment_date', 'graduation_year', 'address', 'city', 'profile_picture')
admin.site.register(User,StudentUser)

class StaffUser(admin.ModelAdmin):
    list_display = ('id_number', 'first_name', 'last_name', 'role', 'email', 'department', 'phone_number', 'profile_picture')
admin.site.register(Staff,StaffUser)