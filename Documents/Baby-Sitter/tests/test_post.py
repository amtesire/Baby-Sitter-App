import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):

    def setUp(self):
        self.user_Ira = User(first_name = "Baby",last_name = "Sitting",username = "babysitting",password = "password",email = "test@gmail.com")
        self.new_post = Post(post_title = "Test Title",post_content = "Hello there,we are testing",user_id = self.user_Baby.id)
        self.new_comment = Comment(comment = "nicee",post_id = self.new_post.id,user_id = self.user_Baby.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Baby, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))
