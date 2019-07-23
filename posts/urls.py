"""URLs for the posts app."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('posts/', views.MessageBoardView.as_view(), name='posts'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',
         views.BlogUpdateView.as_view(), name='post_edit'),
]
