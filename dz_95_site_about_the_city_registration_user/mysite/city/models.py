from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='city/images/')
    views = models.IntegerField()

