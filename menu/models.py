from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    

class Food(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='food_items',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-category']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name