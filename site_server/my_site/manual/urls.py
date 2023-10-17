from django.urls import path
from .views import main_manual, manual

appname = "manual"

urlpatterns = [
    path('', main_manual, name='manual'),
    path('/<int:chapter>', manual, name='chapter')
]