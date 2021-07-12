from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from posts.models import Post

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to="account/", blank=True)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f"{self.user.username} profile"

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls, id):
        delete = Profile.objects.filter(id=id).delete()
        return True
