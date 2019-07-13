"""URLs for the posts app."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('posts/', views.MessageBoardView.as_view(), name='posts'),
]
