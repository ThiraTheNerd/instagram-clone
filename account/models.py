from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from posts.models import Post
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255, null=True)
    bio = HTMLField("bio", blank=True)
    profile_pic = CloudinaryField("profile_pic")
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f"{self.user.username} profile"

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    @classmethod
    def search_by_name(cls, search):
        user = User.objects.filter(username__icontains=search)
        print(user)
        profile = Profile.objects.get(user=user)
        return profile

    @classmethod
    def delete_profile(cls, id):
        delete = Profile.objects.filter(id=id).delete()
        return True
