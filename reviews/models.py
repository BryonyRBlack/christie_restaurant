from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return f"Review by {self.user.username} - {self.title}"
