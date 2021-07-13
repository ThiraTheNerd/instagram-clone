from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from account.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from account.views import profile

# Create your views here.
# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):
    """
    Function that returns the index page
    try:
    editor = Editor.objects.get(email = 'example@gmail.com')
    print('Editor found')
    except DoesNotExist:
    print('Editor was not found')
    """
    posts = Post.objects.all()
    users = Profile.objects.all()
    return render(request, "index.html", {"posts": posts, "users": users})
