from timeit import default_timer

from django.shortcuts import render
from django.http import HttpRequest


def home_page(request: HttpRequest):
    context = {

    }
    return render(request, 'app/main-page.html', context=context)


def auth_view(request: HttpRequest):
    context = {

    }
    return render(request, 'myauth/auth.html', context=context)