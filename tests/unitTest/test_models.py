from django.test import TestCase
from client.models import Post
from tests.unitTest.fixture import generate_title, generate_description, POST_COUNT

class PostModelTest(TestCase):

    @classmethod
    # set up test data
    def setUpTestData(cls):
        for i in range(1,POST_COUNT+1):
            Post.objects.create(title=generate_title(i),description=generate_description(i))

    # get all posts test
    def test_get_all_posts(self):
        posts=Post.objects.all()
        self.assertEqual(len(posts),POST_COUNT)

    # get post by title test
    def test_get_post_by_title(self):
        for i in range(1,POST_COUNT+1):
            post=Post.objects.get(title=generate_title(i))
            self.assertEqual(post.title,generate_title(i))

    # get post by id test
    def test_get_post_by_id(self):
        for i in range(1,POST_COUNT+1):
            post=Post.objects.get(id=i)
            self.assertEqual(post.id,i)

    # update post title test
    def test_update_post_title(self):
        post=Post.objects.get(title=generate_title(1))
        post.title="Why we study django?"
        post.save()
        self.assertEqual(post.title,"Why we study django?")

    # check default value of likecount & dislikecount data test
    def test_check_default_data_of_likecount_and_dislikecount(self):
        posts=Post.objects.all()
        for post in posts:
             self.assertEqual(post.likecount,0)
             self.assertEqual(post.dislikecount,0)

    # update likecount and dislikecount test
    def test_update_likecount_and_dislikecount(self):
        post=Post.objects.get(id=1)
        post.likecount=1
        post.save()
        self.assertEqual(post.likecount,1)
        post.dislikecount=1
        post.save()
        self.assertEqual(post.dislikecount,1)

    # delete post by id test
    def test_delete_post_by_id(self):
        post=Post.objects.get(id=1)
        post.delete()
        try:
            post=Post.objects.get(id=1)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e,Post.DoesNotExist)


