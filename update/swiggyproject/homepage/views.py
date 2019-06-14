from django.shortcuts import render
from django import forms
from django.views import View,generic
from django.conf import settings
from restaurant.models import Restaurant
from dishes.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class Test(View):
	def get(self,request):
		x=Restaurant.objects.filter(flag='1').order_by('id')
		y=Restaurant.objects.filter(flag='1').order_by('-id')
		paginator=Paginator(x,6)
		page = request.GET.get('page')
		try:
			names=paginator.page(page)
		except PageNotAnInteger:
			names=paginator.page(1)
		except EmptyPage:
			names=paginator.page(paginator.num_pages)
		return render(request,'homepage/index.html',{"names":names,'x':y}) 

class Food(View):
	def get(self,request):
		id1=request.GET.get('id')
		x=Dishes.objects.filter(restaurant_id=id1)
		print(x)
		paginator=Paginator(x,6)
		page = request.GET.get('page')
		try:
			names=paginator.page(page)
			print(names)
		except PageNotAnInteger:
			names=paginator.page(1)
			print(names)
		except EmptyPage:
			names=paginator.page(paginator.num_pages)
			print(names)
		return render(request,'homepage/food.html',{"names":names,'id':id1}) 

class SearchHomeView(View):
	def get(self,request):
		search=request.GET.get('searchinput')
		print('searchview')
		restaurant1=Restaurant.objects.filter(restaurantname__contains=search)
		print(restaurant1)
		#dishname=Dishes.objects.filter(dishname__contains=search)
		#d = getVariables(request)
		#d['restaurant']=restaurant
		return render(request,'homepage/search.html',{'restaurant1':restaurant1})

def searchResults(request):
	try:
		print('enter')
		search=request.GET.get('searchinput')
		print('search=',search)
		restaurant1=Restaurant.objects.filter(restaurantname__contains=search)
		print(restaurant1[0].id)
		#dishname=Dishes.objects.filter(dishname__contains=search)
		#d = getVariables(request)
		#d['restaurant']=restaurant
		return render(request,'homepage/search.html',{'restaurant1':restaurant1})

	except Exception as e:
		print ('%s (%s)' % (e.message, type(e)))

		