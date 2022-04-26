from turtle import title
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title