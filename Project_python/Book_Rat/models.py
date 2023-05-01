from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=2000)
    cover = models.CharField(max_length=1000)
    def __str__(self):
        return self.title


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

class Cart(models.Model):
    user = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)