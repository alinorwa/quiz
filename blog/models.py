from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author      = models.ForeignKey(User ,on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    img         = models.ImageField(upload_to='images/')
    date        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title} = {self.text[:30]} ...."    