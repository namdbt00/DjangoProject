from django.db import models


# Create your models here.
class Books (models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.BigIntegerField()
    amount = models.IntegerField()
