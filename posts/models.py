from django.db import models
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from .models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return self.post


class Post(models.Model):
    image = models.ImageField(upload_to="posts/")
    caption = HTMLField()
    user = models.OneToOneField(User, on_delete=CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return f"{self.id}_{self.post_date}_by_{self.user.username}"

    class Meta:

        ordering = ["-image"]

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
