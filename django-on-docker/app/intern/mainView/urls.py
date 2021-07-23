from django.urls import path
from ..mainView.view import MainPage

urlpatterns = [
    path('', MainPage.as_view()),
]