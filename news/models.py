from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    excerpt = models.TextField(blank=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return f"Comment {self.body} by {self.user}"