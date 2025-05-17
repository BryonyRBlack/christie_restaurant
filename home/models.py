from django.db import models
from cloudinary.models import CloudinaryField

'''
This model is for the home page.
It has a Title and content, for the user to be able to read when opening the page. It does not request further information
'''

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=200)
    side_image = CloudinaryField("image", default="placeholder")
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title