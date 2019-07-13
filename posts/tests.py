"""Test cases for posts app."""
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='A nice title',
            body='OK',
            author=self.user
        )

    def test_string_representation(self):
        """Test post creation with title."""
        post = Post.objects.create(title='A nice title')
        self.assertEqual(str(post), post.title)


class HomePageViewTest(TestCase):
    """Test homepage view."""
    def setUp(self):
        Post.objects.create(text='another test')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class AboutPageViewTest(TestCase):
    """Test homepage view."""
    def setUp(self):
        Post.objects.create(text='About Page Test')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


class PostsPageViewTest(TestCase):
    """Test homepage view."""
    def setUp(self):
        Post.objects.create(text='Posts Page Test')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')
