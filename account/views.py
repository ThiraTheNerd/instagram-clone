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


def search_results(request):
    if "user" in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        try:
            searched_user = Profile.search_results(search_term)
        except ObjectDoesNotExist:
            raise Http404()
        return redirect(profile, username=search_term)
