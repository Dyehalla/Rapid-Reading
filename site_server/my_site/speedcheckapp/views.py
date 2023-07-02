from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .my_scripts import random_text, time_converter
from speedcheckapp.models import Result
from .questions import links, answers


class StartView(TemplateView):
    template_name = 'speedcheckapp/speed-check-start.html'


def test_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        read_list = request.COOKIES.get('read')
        if read_list:
            text_data = random_text(read_list)
        else:
            text_data = random_text('1/2/3/4/5/6/7/8/9/10')
        context = {
            'text': text_data['text'],
            'title': text_data['title']
        }
        request.session['words'] = text_data['length']

        request.session['title'] = text_data['title']

        response = render(request, 'speedcheckapp/test.html', context=context)
        response.set_cookie('read', text_data['new_read_list'])
        return response

    request.session['time'] = request.POST.get('time')
    return redirect('questions')


def result_view(request):
    context = dict()
    time = request.session.get('time')
    words = request.session.get('words')
    correct_answers = request.session.get('correct_answers')

    if time:
        context['words'] = words
        context['speed'], context['minutes'], context['seconds'] = time_converter(time, words)

    if correct_answers:
        context['correct_answers'] = correct_answers
    else:
        context['correct_answers'] = 0

    return render(request, 'speedcheckapp/result.html', context=context)


def save_view(request: HttpRequest):
    if request.session.get('time'):
        time = request.session.get('time')
        words = request.session.get('words')
        speed, minutes, seconds = time_converter(time, words)
        Result.objects.create(user_profile=request.user.profile, time=f'{minutes}м {seconds}с',
                              speed=speed)
    return redirect('home')


def questions_view(request: HttpRequest):
    title = request.session.get('title')
    if not title:
        return HttpRequest('Пожалуйста, включите cookie, а то без них вообще ничего не работает')
    if request.method == 'GET':
        questions = list(links.get(title).items())
        context = {
            'q1': questions[0][0],
            'o1': questions[0][1],

            'q2': questions[1][0],
            'o2': questions[1][1],

            'q3': questions[2][0],
            'o3': questions[2][1],

            'q4': questions[3][0],
            'o4': questions[3][1],

            'q5': questions[4][0],
            'o5': questions[4][1],
        }
        return render(request, 'speedcheckapp/questions.html', context=context)

    my_answers = set(list(request.POST.keys()))
    correct_answers = answers[request.session.get('title')]

    request.session['correct_answers'] = len(my_answers.intersection(correct_answers))
    return redirect('result')
