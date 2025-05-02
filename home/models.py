from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title