"""Views of posts."""
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


class PostListView(ListView):
    """List all the posts."""
    model = Post
    template_name = 'home.html'


class AboutPageView(TemplateView):
    """The About Page."""
    template_name = 'about.html'


class MessageBoardView(ListView):
    """The Message Board."""
    model = Post
    template_name = 'posts.html'


class BlogDetailView(DetailView):
    """View for individual blog."""
    model = Post
    template_name = 'post_detail.html'
