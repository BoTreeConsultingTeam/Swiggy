from django.db import models
from city_and_state.models import *
from users.models import *
from restaurant.models import *
from .models import *
class DishesType(models.Model):
	dish_type_name=models.CharField(null=True,max_length=30)

	def __str__(self):
		return self.dish_type_name

class Dishes(models.Model):
	restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
	dish_type=models.ForeignKey(DishesType,on_delete=models.CASCADE,null=True)
	dishname=models.CharField(null=True,max_length=30)
	veg_or_nonveg=models.CharField(max_length=6)
	img=models.ImageField(upload_to='images/',default='default.png')
	dishinfo=models.CharField(null=True,max_length=1024)
	price=models.CharField(null=True,max_length=1024)

	def __str__(self):
		return self.dishname

