from django.contrib.auth.models import User
from account.models import Profile
from django.test import TestCase
from posts.models import Post

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        post = Post(image="pun.jpeg", caption="I love today").save_post()
        self.test_prof = Profile(
            bio="I love God", profile_pic="cross.jpeg", posts=1, user_id=2
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.test_prof, Profile))

    def test_save_profile(self):
        self.test_prof.save_profile()
        users = Profile.objects.all()
        self.assertTrue(len(users) > 2)
