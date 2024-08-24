from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/registration.html', context={'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/registration.html', context={'form': form})
        User.objects.create_user(
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            password=form.cleaned_data.get('password')
        )
        return redirect('/')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        if not user:
            form.add_error(None, 'Wrong username or password')
            return render(request, 'user/login.html', context={'form': form})
        login(request, user)
        return redirect('/')


@login_required(login_url='logout_view')
def logout_view(request):
    logout(request)
    return redirect('/')
