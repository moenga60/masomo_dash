from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('', views.users, name='users'),
    path('add-student/', views.add_student, name='add_student'),
    path('success/', views.success, name='success'),
    path('add-staff/', views.add_staff, name='add_staff'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)