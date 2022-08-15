from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Chat
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# user sign up
def signupUser(request):
    if not request.user.is_authenticated:   # prevents authenticated user from signup
        if request.method =='POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                user = fm.save()
                login (request, user)     
                return redirect('home')      
        else:
            fm = SignupForm()
        return render(request, 'signup.html', {'form':fm})
    else:
        return redirect('home')

# user authentication & login
def loginUser(request):
    if not request.user.is_authenticated:   # prevents authenticated user from login
        if request.method == 'POST':
            fm = LoginForm(request = request, data = request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            fm = LoginForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return redirect('home')   

def home(request):
    room  = Room.objects.all()
    return render(request, 'home.html', {'rooms':room})

# logout user
def logoutUser(request):
    logout(request)
    return redirect('/')