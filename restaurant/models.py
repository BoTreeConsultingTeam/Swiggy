from django.db import models
from city_and_state.models import *
from users.models import *
# Create your models here.
class Restaurant(models.Model):
	ownername=models.CharField(null=True,max_length=30)
	restaurantname=models.CharField(null=True,max_length=30)
	bank_account_no=models.CharField(max_length=1024)
	state=models.ForeignKey(State,on_delete=models.CASCADE,null=True)
	city=models.ForeignKey(City,on_delete=models.CASCADE,null=True)
	address=models.CharField(max_length=1024)
	img=models.ImageField(upload_to='images/',default='default.png')
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
	flag=models.CharField(max_length=30,default=0)

	def __str__(self):
		return self.restaurantname