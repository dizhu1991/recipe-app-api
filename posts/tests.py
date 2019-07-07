"""Test cases for posts app."""
from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just testing')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.text
        self.assertEqual(expected_object_name, 'just testing')


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
