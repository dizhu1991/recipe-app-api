"""Views of posts."""
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

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


class BlogCreateView(CreateView):
    """View for creating a new blog post."""
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    """Edit a blog post."""
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
