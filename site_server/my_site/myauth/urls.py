from django.urls import path
from .views import MyLogoutView, login_view, RegisterView

appname = "myauth"

urlpatterns = [
    path('logout', MyLogoutView.as_view(), name='logout'),
    path('reg', RegisterView.as_view(), name='reg'),
    path('login', login_view, name='login'),
]