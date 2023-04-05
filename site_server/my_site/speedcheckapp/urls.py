from django.urls import path

from speedcheckapp.views import StartView, test_view, ResultView

urlpatterns = [
    path('', StartView.as_view(), name='start'),
    path('test', test_view, name='test'),
    path('result', ResultView.as_view(), name='result')
]