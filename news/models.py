from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


'''
This model allows for articles to be created.
It requires a title, slug, body, except.
It also allows for if this has been published or not, and that status.
The meta class allows it to be ordered
with the most recently posted at the start
'''


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Article(models.Model):
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


'''
The comment model allows for users to leave a comment on the page.
It confirms the article the comment is being left on.
The user must be logged in, and they are able to leave a message,
as well as rate the article out of 5.
The class meta allows these to be shown with the newest first.
'''


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="commenter")
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i)
                                                       for i in range(1, 6)])
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return f"Comment {self.body} by {self.user}"
