from django.db import models

class Blogs (models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)