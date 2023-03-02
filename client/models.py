from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likecount = models.IntegerField(default=0)
    dislikecount = models.IntegerField(default=0)
    def __str__(self):
        return self.title
