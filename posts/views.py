from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from account.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, HttpResponse
from account.views import profile
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# Create your views here.
@login_required(login_url="/accounts/login/")
@csrf_exempt
def index(request):
    """
    Function that returns the index page
    """
    if request.method == "POST":
        if request.POST.get("operation") == "like_submit" and request.is_ajax():
            content_id = request.POST.get("content_id", None)
            content = get_object_or_404(Post, pk=content_id)
            if content.likes.filter(id=request.user.id):
                content.likes.remove(request.user)
                liked = False
            else:
                content.likes.add(request.user)
                liked = True
            ctx = {
                "likes_count": content.total_likes,
                "liked": liked,
                "content_id": content_id,
            }
            return HttpResponse(json.dumps(ctx), content_type="application/json")

    posts = Post.objects.all()
    users = Profile.objects.all()
    all_comments = Comment.objects.all()
    already_liked = []
    id = request.user.id
    for post in posts:
        if post.likes.filter(id=id).exists():
            already_liked.append(post.id)
    ctx = {
        "posts": posts,
        "users": users,
        "all_comments": all_comments,
        "already_liked": already_liked,
    }
    return render(request, "index.html", ctx)


@login_required(login_url="/accounts/login/")
def view_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
        print(post)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, "posts/single-post.html")


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
    return redirect("view_post", pk=post_id)
