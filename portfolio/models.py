from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=350)
    message = models.TextField()