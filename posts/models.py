"""Posts model."""
from django.db import models


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """String representation of a post."""
        return self.text[:50]
