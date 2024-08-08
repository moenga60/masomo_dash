from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User
from .forms import UserForm

@login_required
def users(request):
    # return render(request, 'index.html')
    users = User.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'users': users,
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

def add_student(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
            form = UserForm
        
    return render(request, 'add_student.html', {'form': form})