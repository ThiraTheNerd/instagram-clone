from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = "user"
        fields = ("fullName", "bio", "profilePic")
