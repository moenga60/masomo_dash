from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User, Staff
from .forms import UserForm, StaffForm
from django.contrib.auth.views import LoginView


@login_required
def users(request):
    users = User.objects.all().values()
    user_count = User.objects.count()
    staff = Staff.objects.all()
    template = loader.get_template('index.html')
    context = {
        'users': users,
        'user_count': user_count,
        'staff': staff,
    }
    return HttpResponse(template.render(context, request))
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('users')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
            # return render(request, 'login.html', {'messages': 'Invalid username or password'})
    
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            return redirect('login')
    else:
            form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def add_student(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
            form = UserForm()
        
    return render(request, 'add_student.html', {'form': form})


def success(request):
    return render(request, 'success.html')

# staff
@login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    
    else:
        form = StaffForm()

    return render(request, 'add_staff.html', {'form': form})


    



