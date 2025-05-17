from django.db import models
from django.contrib.auth.models import User

'''
Model created for ease of being able to get in contact.
This can be sent without an account being required.
Requests name and email, before the message is input.
'''
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"