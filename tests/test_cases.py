from django.test import TestCase
from django.urls import reverse
from client.models import Post

class ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='title1', description='description1')
        Post.objects.create(title='title2', description='description2')
        Post.objects.create(title='title3', description='description3')

    def test_posts_are_rendering_on_home_page(self):
        response = self.client.get(reverse('home'))
        print(response.content)
        self.assertContains(response, 'title1')
        self.assertContains(response, 'title2')
        self.assertContains(response, 'title3')

    def test_rendering_like_and_dislike_button_with_correct_data(self):
        response = self.client.get(reverse('home'))
        for i in range(1,4):
            self.assertContains(response, f'id="button1" onclick="reviewPost(\'{i}\',1)')
            self.assertContains(response, f'id="button2" onclick="reviewPost(\'{i}\',0)')

    def test_likecount_is_increasing_on_isLike_have_value_one(self):
        response= self.client.post('/api/review/1/',{'isLiked':1})
        post=Post.objects.get(id=1)
        self.assertEqual(post.likecount,1)
        response= self.client.post('/api/review/1/',{'isLiked':1})
        post=Post.objects.get(id=1)
        self.assertEqual(post.likecount,2)

    def test_dislikecount_is_increasing_on_isLike_have_value_zero(self):
        response= self.client.post('/api/review/1/',{'isLiked':0})
        post=Post.objects.get(id=1)
        self.assertEqual(post.dislikecount,1)
        response= self.client.post('/api/review/1/',{'isLiked':0})
        post=Post.objects.get(id=1)
        self.assertEqual(post.dislikecount,2)