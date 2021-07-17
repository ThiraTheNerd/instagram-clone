from django.db import models
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    image = CloudinaryField("image")
    caption = HTMLField()
    user = models.OneToOneField(User, on_delete=CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")

    def __str__(self):
        return f"{self.id}_{self.post_date}_by_{self.user.username}"

    class Meta:

        ordering = ["-image"]

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    comment = models.TextField(blank=True, null=True)
    post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name="comments", null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.comment}"
