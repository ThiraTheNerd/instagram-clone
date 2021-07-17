from django.http.response import Http404
from account.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm, ProfileForm
from django.contrib import messages
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return "/"


# Create your views here.
@login_required(login_url="accounts/login")
def profile(request, username):
    user = User.objects.get(username=username)
    currentuser = request.user
    try:
        profile = Profile.objects.get(user=user.id)
        posts = profile.posts.all()
    except ObjectDoesNotExist:
        raise Http404()

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ("Your profile was successfully updated!"))
        return redirect("profile", user.username)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)
    return render(
        request,
        "registration/profile.html",
        {
            "profile": profile,
            "posts": posts,
            "currentuser": currentuser,
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


def edit_profile(request):
    return render(request, "registration/update_profile.html")
