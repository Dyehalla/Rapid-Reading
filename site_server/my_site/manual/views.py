from os import path
from django.http import HttpRequest
from django.shortcuts import render


def main_manual(request: HttpRequest):
    return manual(request, chapter=1)


def manual(request: HttpRequest, chapter):
    file = open(path.abspath('../manual_db.csv'), 'r')
    data = file.readlines()[chapter - 1].split(';')
    file.close()
    head = data[0]
    paragraph = data[1]

    context = {
        'head': head,
        'paragraph': paragraph
    }
    return render(request, 'manual/manual.html', context=context)
