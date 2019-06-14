from django.db import models
from users.models import CustomUser
from restaurant.models import Restaurant
from dishes.models import *
# Create your models here.
class Cart(models.Model):
	restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
	dish=models.ForeignKey(Dishes,on_delete=models.CASCADE,null=True)
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
	quantity=models.CharField(null=True,max_length=30)
	
class Orders(models.Model):
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
	restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
	orderstatus=models.CharField(null=True,max_length=30)
	totalpricetax=models.CharField(null=True,max_length=30)
	orderdate=models.DateTimeField(auto_now_add=True)
	

class OrdersItems(models.Model):
	orders=models.ForeignKey(Orders,on_delete=models.CASCADE,null=True)
	dish=models.ForeignKey(Dishes,on_delete=models.CASCADE,null=True)
	quantity=models.CharField(null=True,max_length=30)
	totalprice=models.CharField(null=True,max_length=30)

class DeliveryAddress(models.Model):
	orders=models.ForeignKey(Orders,on_delete=models.CASCADE,null=True)
	deliveryaddress=models.CharField(max_length=1000,default=0)

