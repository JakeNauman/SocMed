from django.db import models

class Post(models.Model):
    username = models.CharField(max_length = 50)
    text = models.CharField(max_length = 180)

    def __str__(self):
        return f'Post from {self.username}'
