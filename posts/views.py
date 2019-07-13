"""Views of posts."""
from django.views.generic import TemplateView, ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class MessageBoardView(ListView):
    model = Post
    template_name = 'posts.html'
