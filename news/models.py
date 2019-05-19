from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Author: {self.author} - Title: {self.title}"