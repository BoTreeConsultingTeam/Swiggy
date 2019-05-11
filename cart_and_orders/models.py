from django.db import models
from users.models import *
from restaurant.models import *
from dishes.models import *
# Create your models here.
class Cart(models.Model):
	restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
	dish=models.ForeignKey(Dishes,on_delete=models.CASCADE,null=True)
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
	quantity=models.CharField(null=True,max_length=30)
	

	
