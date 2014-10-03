from django.db import models

# Create your models here.

class Customer(models.Model):
    number = models.CharField(max_length=10, )
    name = models.CharField(max_length=255)
    date = models.DateTimeField('date registered')
    

class Supplier(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    date = models.DateTimeField('date registered')
    
    
class CustomerBatch(models.Model):
    customer = models.ForeignKey(Customer)
    description = models.CharField(max_length=255)
    date = models.DateTimeField('date registered')
    price = models.FloatField()

class SupplierBatch(models.Model):
    supplier = models.ForeignKey(Supplier)
    description = models.CharField(max_length=255)
    date = models.DateTimeField('date registered')
    price = models.FloatField()
    