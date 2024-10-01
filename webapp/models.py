from django.db import models

# Create your models here.
class contactdb(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    message = models.TextField(max_length=100, null=True, blank=True)
class signindb(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    user_name = models.CharField(max_length=50, null=True, blank=True)
    product_name = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField( null=True, blank=True)
    price=models.IntegerField( null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
class orderdb(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField( null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    order_notes = models.CharField(max_length=50, null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)

