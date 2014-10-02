from django.db import models

# Create your models here.

class Customer(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    date = models.DateTimeField('date registered')
    

class Supplier(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    date = models.DateTimeField('date registered')