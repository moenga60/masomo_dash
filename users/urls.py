from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('', views.users, name='users'),
    path('add-student/', views.add_student, name='add_student'),
    # path('students/', views.student_list, name='student_list'),
    
]