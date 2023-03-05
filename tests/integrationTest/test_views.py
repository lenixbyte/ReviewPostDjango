from django.test import TestCase
from django.urls import reverse
from client.models import Post

class ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_posts = 10
        for post_num in range(number_of_posts):
            Post.objects.create(
                title=f'Why django? {post_num}',
                description=f'Because it is fast {post_num}'
            )

    def test_post_data_rendering_in_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Why django?')
        self.assertContains(response, 'Because it is fast')

    def test_api_url_exists_for_all_posts(self):
        for i in range(1,10):
            response = self.client.get(f'/api/review/{i}/')
            self.assertEqual(response.status_code, 200)

    def test_onclick_in_button_on_each_post_is_working(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'onclick')
        self.assertContains(response, 'isLike')

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