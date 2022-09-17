from django.db import models

# Create your models here.
class Product(models.Model):
     name = models.CharField(max_length=100)
     price = models.FloatField()
     image = models.ImageField(upload_to='images')
     size = models.CharField(max_length=50)
     description = models.CharField(max_length=100)