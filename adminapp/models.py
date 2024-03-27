from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20, default="empty")
    description=models.CharField(max_length=20)
    image=models.ImageField(upload_to='image',default='null.jpg')

class product(models.Model):
    name=models.CharField(max_length=10)
    image=models.ImageField(upload_to='image',default='null.jpg')
    category=models.TextField(max_length=20)
    price=models.IntegerField()
    description=models.TextField(max_length=30,default="empty")
    
