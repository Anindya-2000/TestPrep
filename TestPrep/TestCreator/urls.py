from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create/', createQP,name='create_q'),
    path('upload/<int:qp>/<str:typeofq>/<int:numberOfquestion>/', uploadQP,name='upload_q'),

]