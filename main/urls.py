from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', indexm, name='indexm'),
    path('series', indexs, name='indexs'),
]