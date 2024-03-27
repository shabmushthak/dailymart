from django.db import models
from adminapp.models import*
# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=10)
    number=models.IntegerField()
    mail=models.TextField(max_length=20)

class register(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    contact=models.IntegerField()
    mail=models.TextField(max_length=20)

class cart(models.Model):
    userid=models.ForeignKey(register,on_delete=models.CASCADE)
    productid=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)

class checkout(models.Model):
    userid=models.ForeignKey(register,on_delete=models.CASCADE)
    cartid=models.ForeignKey(cart,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100,default="")
    country=models.CharField(max_length=20)
    postal_zip=models.CharField(max_length=20)
    
