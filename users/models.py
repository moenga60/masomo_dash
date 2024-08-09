from django.db import models
# from django.contrib.auth.models import AbstractUser

class User(models.Model):
    registration_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    graduation_year = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    def __str__(self):
        return self.first_name
        

    
    
    