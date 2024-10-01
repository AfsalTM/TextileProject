from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="category_image",null=True,blank=True)
class Products(models.Model):
    category_name = models.CharField(max_length=50, null=True, blank=True)
    product_name = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    image1 = models.ImageField(upload_to="product_image",null=True,blank=True)
    image2 = models.ImageField(upload_to="product_image", null=True, blank=True)
    image3 = models.ImageField(upload_to="product_image", null=True, blank=True)
class orderdb(models.Model):
    pass
