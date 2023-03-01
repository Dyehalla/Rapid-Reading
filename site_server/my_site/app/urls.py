from django.urls import path
from .views import home_page, auth_view

appname = "app"

urlpatterns = [
    path("", home_page, name='home'),
    path('auth/', auth_view, name='auth')
]