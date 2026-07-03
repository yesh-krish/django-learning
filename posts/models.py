from datetime import date

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(null = False, blank = True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
