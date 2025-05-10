from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Food(models.Model):
    category = models.ForeignKey(
        Category,
        related_query_name='food_items',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name