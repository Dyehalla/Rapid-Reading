from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import LoginForm


def auth_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'myauth/auth.html')

    if request.POST.get('username'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')

        return render(request, 'myauth/auth.html', context={'error': 'Invalid data'})

    username = request.POST['regusername']
    if User.objects.filter(username=username).exists():
        return render(request, 'myauth/auth.html', context={'error': 'Already exists'})
    password = request.POST['regpassword1']
    User.objects.create(username=username, password=password)
    user = User.objects.get(username=username, password=password)
    login(request, user=user)
    return redirect('/')


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('auth'))