from django.urls import path, include
from .views import HomePage

appname = "app"

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path('auth/', include('myauth.urls'))
]