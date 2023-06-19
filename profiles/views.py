from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import MyAuthenticationForm, MyUserCreationForm


def login_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'firstly you should logout')
        return redirect('profiles:logout')
    form = MyAuthenticationForm()
    if request.method == "POST":
        form = MyAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, f"{user.username} was successfully logged in")
                return redirect('home:home')
            messages.error(request, f"your account didn't logged in")
            return redirect(".")
        messages.error(request, f"your account didn't logged in")
        return redirect(".")
    ctx = {
        'form': form
    }
    return render(request, 'profiles/login.html', ctx)


def create_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'firstly you should logout')
        return redirect('profiles:logout')
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f"{obj.username} was successfully registered")
            return redirect('home:home')
        messages.error(request, "fields must not be empty")
        return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'profiles/register.html', ctx)


def logout_user(request):
    if not request.user.is_authenticated:
        messages.info(request, 'firstly you should login')
        return redirect('profiles:login')
    if request.method == "POST":
        user = request.user
        logout(request)
        messages.success(request, f"{user.username} was successfully logged out")
        return redirect('home:home')
    return render(request, 'profiles/logout.html')
