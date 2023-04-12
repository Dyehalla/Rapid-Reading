from django.urls import path, include
from .views import HomePage, my_results_view

appname = "app"

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path('auth/', include('myauth.urls')),
    path('profile/results', my_results_view, name='my_results'),
]