from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # description = models.CharField(max_length=800)
    # cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title

