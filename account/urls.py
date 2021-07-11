from django.conf.urls import url
from django.shortcuts import render
from . import views

# Create your views here.
urlpatterns = [
    url("^$", views.index, name="index"),
]
