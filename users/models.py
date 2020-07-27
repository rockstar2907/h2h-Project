from django.db import models

# Create your models here.

class UserDetails(models.Model):
    username=models.CharField(max_length=30)
    phno=models.CharField(max_length=15)
    address=models.CharField(max_length=300)
class Restaurants(models.Model):
    rest_name=models.CharField(max_length=99,primary_key=True)
    address=models.CharField(max_length=150)
class Items(models.Model):
    #use foriegn key from restaurants.
    id = models.AutoField(primary_key=True)
    rest_name=models.ForeignKey('Restaurants',on_delete=models.CASCADE,)
    item_name=models.CharField(max_length=100)
    price=models.IntegerField()

class UserOrders(models.Model):
    username=models.CharField(max_length=30)
    item_id=models.IntegerField()
    item_name=models.CharField(max_length=50)
    qty=models.IntegerField()
    price=models.IntegerField()
    rest_name=models.CharField(max_length=100)
class CurrentOrders(models.Model):
    username=models.CharField(max_length=30)
    phno=models.CharField(max_length=15)
    address=models.CharField(max_length=300)
    items=models.CharField(max_length=500)
    rest_name=models.CharField(max_length=100)
    total_amount=models.IntegerField()
class AllOrders(models.Model):
    username=models.CharField(max_length=30)
    phno=models.CharField(max_length=15)
    address=models.CharField(max_length=300)
    items=models.CharField(max_length=500)
    rest_name=models.CharField(max_length=100)
    total_amount=models.IntegerField()
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    item_id=models.ForeignKey(Items,on_delete=models.CASCADE,)
    item_name=models.CharField(max_length=50)    
    price=models.IntegerField()
    qty=models.IntegerField()
    rest_name=models.CharField(max_length=100)