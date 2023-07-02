from django.urls import path

from .views import StartView, test_view, result_view, save_view, questions_view

urlpatterns = [
    path('', StartView.as_view(), name='start'),
    path('test', test_view, name='test'),
    path('result', result_view, name='result'),
    path('result/save', save_view, name='save'),
    path('test/questions', questions_view, name='questions')
]