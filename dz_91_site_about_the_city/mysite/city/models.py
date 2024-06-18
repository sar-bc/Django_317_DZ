from django.db import models


# Create your models here.
class Attractions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='city/images/')

