from django.urls import path
from .views import home_index

appname = "app"

urlpatterns = [
    path("", home_index, name='home')
]