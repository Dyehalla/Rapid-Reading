from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .my_scripts import random_text, time_converter
from speedcheckapp.models import Result


class StartView(TemplateView):
    template_name = 'speedcheckapp/speed-check-start.html'


def test_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        read_list = request.COOKIES.get('read')
        if read_list:
            text_data = random_text(read_list)
        else:
            text_data = random_text('1/2/3/4/5/6/7')
        context = {
            'text': text_data['text'],
            'title': text_data['title']
        }
        request.session['words'] = text_data['length']
        response = render(request, 'speedcheckapp/test.html', context=context)
        response.set_cookie('read', text_data['new_read_list'])
        return response

    request.session['time'] = request.POST.get('time')
    return redirect('result')


def result_view(request):
    context = dict()
    time = request.session.get('time')
    words = request.session.get('words')
    if time:
        context['words'] = words
        context['speed'], context['minutes'], context['seconds'] = time_converter(time, words)

    return render(request, 'speedcheckapp/result.html', context=context)


def save_view(request: HttpRequest):
    if request.session.get('time'):
        time = request.session.get('time')
        words = request.session.get('words')
        speed, minutes, seconds = time_converter(time, words)
        Result.objects.create(user_profile=request.user.profile, time=f'{minutes}м {seconds}с',
                              speed=speed)
    return redirect('home')
