from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    full_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "full_name", "username", "password1", "password2"]
