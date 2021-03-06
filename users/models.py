from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from city_and_state.models import *
class CustomUser(AbstractUser):
	email=models.EmailField(unique=True)
	contact=models.IntegerField(null=True)
	state=models.ForeignKey(State,on_delete=models.CASCADE)
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	address=models.CharField(max_length=1024)
	pincode=models.IntegerField(null=True)
	ownnershipstatus=models.CharField(null=True,max_length=30,default='normaluser')
	count=models.CharField(max_length=30,default=0)