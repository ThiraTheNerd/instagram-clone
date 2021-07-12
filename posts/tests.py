from django.contrib.auth.models import User
from posts.models import Post
from django.test import TestCase

# Create your tests here.
class PostsTestClass(TestCase):
    def setUp(self):
        """
        Creating a new posts instance
        """
        self.newpost = Post(image="pun.jpeg", caption="I love today", user="jackson")
        self.newpost.save_post()

    def test_savepost(self):
        self.newpost.save_post()
        post_list = Post.objects.all()
        self.assertTrue(len(post_list) > 0)

    def test_delete(self):
        """
        Test the delete method in posts model
        """
        self.newpost.save_post()
        self.newpost.delete_post()
        newpost = Post.objects.get(user=1)
        self.assertTrue(newpost == 0)
