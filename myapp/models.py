from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class products(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE,default='root')
    name=models.CharField(max_length=50)
    id=models.IntegerField(primary_key=True)
    price=models.FloatField()
    catageory=models.CharField(max_length=30)
    subCatageory=models.CharField(max_length=30)
    image= models.ImageField(upload_to='static/img')
    quentity=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    brand=models.CharField(max_length=10)
    longDescription=models.CharField(max_length=1000)
    rating=models.FloatField(default='0')
    offer=models.BooleanField(default=False)
    warrenty=models.BooleanField(default=False)
    age=models.PositiveIntegerField(default=0)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ManyToManyField(products)
    full_name=models.CharField(max_length=30)
    phone=models.IntegerField()
    address1=models.CharField(max_length=30)
    address2=models.CharField(max_length=50)
    city=models.CharField(max_length=15)
    country=models.CharField(max_length=10)
    zipcode=models.IntegerField()
    note=models.CharField(max_length=50)
    def add_product(self,product):
        self.product.add(product)

class Wishlist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product =models.ManyToManyField(products)


    def add_product(self,product):
        self.product.add(product)
    