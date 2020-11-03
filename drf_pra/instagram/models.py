from django.db import models


class Basic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(Basic):
    message = models.TextField()

