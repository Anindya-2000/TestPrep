from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('jeemains/', views.testView, name='mains-test-view'),
]
