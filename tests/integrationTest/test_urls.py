from django.test import TestCase
from client.urls import urlpatterns
from client.models import Post
from django.urls import reverse

class UrlsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_posts = 10
        for post_num in range(number_of_posts):
            Post.objects.create(
                title=f'Why django? {post_num}',
                description=f'Because it\'s fast {post_num}'
            )

    def test_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_api_url_exists_at_desired_location(self):
        response = self.client.get('/api/review/')
        self.assertEqual(response.status_code, 200)

    def test_api_url_exists_for_all_posts(self):
        for i in range(1,10):
            response = self.client.get(f'/api/review/{i}/')
            self.assertEqual(response.status_code, 200)
