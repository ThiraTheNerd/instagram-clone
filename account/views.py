from django.http.response import Http404
from account.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def profile(request, username):
    user = User.objects.get(username=username)
    try:
        profile = Profile.objects.get(user=user.id)
        posts = profile.posts.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(
        request, "registration/profile.html", {"profile": profile, "posts": posts}
    )


def edit_profile(request):
    return render(request, "registration/update_profile.html")
