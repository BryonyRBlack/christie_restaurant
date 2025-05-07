from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=200)
    side_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title