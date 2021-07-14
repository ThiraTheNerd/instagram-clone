from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
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


def search_results(request):
    if "user" in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        try:
            searched_user = Profile.search_by_name(search_term)
            posts = searched_user.posts.all()
            print(posts)
        except ObjectDoesNotExist:
            raise Http404()
        return render(
            request, "search.html", {"searched_user": searched_user, "posts": posts}
        )


def new_comment(request, post_id):
    current_user = request.user
    if request.method == "POST":
        comment = request.POST.get("comment")
    post = Post.objects.get(id=post_id)
    user_profile = User.objects.get(username=current_user.username)
    Comment.objects.create(comment=comment, post=post, user=user_profile)
    return redirect("index")
