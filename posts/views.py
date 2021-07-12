from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", {"posts": posts})
