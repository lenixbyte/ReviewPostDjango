from django.test import TestCase
from client.models import Post

class PostModelTest(TestCase):

    @classmethod
    # set up test data
    def setUpTestData(cls):
        Post.objects.create(title="Why django?",description="Because it's fast")
        Post.objects.create(title="Django Rocks",description="Everyone Shocks")

    # get all posts test
    def test_get_all_posts(self):
        posts=Post.objects.all()
        self.assertEqual(len(posts),2)

    # get post by title test
    def test_get_post_by_title(self):
        post=Post.objects.get(title="Why django?")
        self.assertEqual(post.title,"Why django?")

    # get post by id test
    def test_get_post_by_id(self):
        post=Post.objects.get(id=1)
        self.assertEqual(post.id,1)

    # update post title test
    def test_update_post_title(self):
        post=Post.objects.get(title="Why django?")
        post.title="Why we study django?"
        post.save()
        self.assertEqual(post.title,"Why we study django?")

    # check default value of likecount & dislikecount data test
    def test_check_default_data_of_likecount_and_dislikecount(self):
        posts=Post.objects.all()
        for post in posts:
             self.assertEqual(post.likecount,0)
             self.assertEqual(post.dislikecount,0)

    # delete post by id test
    def test_delete_post_by_id(self):
        post=Post.objects.get(id=1)
        post.delete()
        try:
            post=Post.objects.get(id=1)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e,Post.DoesNotExist)

