"""Test cases for posts app."""
from django.test import TestCase

from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just testing')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.text
        self.assertEqual(expected_object_name, 'just testing')
