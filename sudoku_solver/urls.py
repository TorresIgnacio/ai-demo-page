from django.urls import path
from . import views

urlpatterns = [
    path('sudoku', views.index),
]
