from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Wanted(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name