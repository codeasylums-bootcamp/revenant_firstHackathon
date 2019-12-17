
from django.db import models

# Create your models here.
class flipkart(models.Model):
    prod_brand = models.CharField(max_length=64, null=True)
    prod_name = models.CharField(max_length=64, null=True)
    prod_price = models.CharField(max_length=64,null=True)
    prod_discount = models.CharField(max_length=64,null=True)

    def __str__(self):
        return self.prod_name

class ajio(models.Model):
    prod_brand = models.CharField(max_length=64, null=True)
    prod_name = models.CharField(max_length=64, null=True)
    prod_price = models.CharField(max_length=64,null=True)
    prod_discount = models.CharField(max_length=64,null=True)

    def __str__(self):
        return self.prod_name