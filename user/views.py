from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user.models import Profile

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/registration.html', context={'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/registration.html', context={'form': form})
        form.cleaned_data.pop('password_confirm')
        image = form.cleaned_data.pop('image')
        user = User.objects.create_user(
            **form.cleaned_data
        )
        Profile.objects.create(user=user, image=image)
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


def profile_view(request):
    if request.method == 'GET':
        posts = request.user.posts.all()
        return render(request, 'user/profile.html', context={'posts': posts})
