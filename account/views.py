from django.http.response import Http404
from account.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def profile(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, "registration/profile.html")
