"""Posts model."""
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, default='Post by default')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    body = models.TextField(null=True)

    def __str__(self):
        """String representation of a post."""
        return self.title
