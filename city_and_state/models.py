from django.db import models
from .models import *
# Create your models here.


class State(models.Model):
	statename=models.CharField(max_length=25,unique=True)

	
	def __str__(self):
		return self.statename


class City(models.Model):
	cityname=models.CharField(max_length=25)
	state=models.ForeignKey(State,on_delete=models.CASCADE)

	def __str__(self):
		return self.cityname
