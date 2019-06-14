from django.shortcuts import render,reverse
from django.views import View,generic
from .models import *
from dishes.models import *
from django.db.models import Q
from django.db.models import *
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import (HttpResponse, HttpResponseNotFound, Http404,HttpResponseRedirect, HttpResponsePermanentRedirect)
# Create your views here.
class AddToCart(View):
	def get(self,request):
		getid=request.GET.get('id')
		print('id=',id)

		a=Dishes.objects.filter(id=getid)
		y=request.user.id
		if getid!=None:
			b=Cart.objects.create(quantity=1,dish_id=getid,restaurant_id=a[0].restaurant.id,user_id=y)
		x=Cart.objects.filter(Q(user_id=y)).order_by('id')
		p=Cart.objects.filter(Q(user_id=y)).aggregate(Count('id'))
		q=1
		print (p)
		if p['id__count']==0:
			q=0
		L=[]
		price={}
		for i in x:
			z,y=int(i.quantity),int(i.dish.price)
			L.append(((z*y)))
			price[i.id]=z*y
		tot=sum(i for i in L)
		
		zipped_list=zip(x,L)
		
		return render(request,'cart_and_orders/cart.html',{'x':x,'price':price,'tot':tot,'q':q})


def pluscart(request):
	if request.is_ajax():
		print('hi')
		userid=request.user.id
		
		quantity=request.GET.get('quantityinput')
		btnid=request.GET.get('btnid')
		if btnid == '+':
			a=int(quantity)+1
			print(a)
		elif btnid == '-':
			a=int(quantity)-1
			print(a)
		
		cartid=request.GET.get('dataid')
		print('quantity=',quantity)
		print('cartid=',cartid)
		Cart.objects.filter( Q(id=cartid)).update(quantity=a)

		x=list(Cart.objects.filter(Q(user_id=userid)).order_by('id'))
		print('x=',x)
		p=Cart.objects.filter(Q(user_id=userid)).aggregate(Count('id'))
		p1=Cart.objects.get(Q(user_id=userid) & Q(id=cartid))
		sibbling=int(p1.quantity)*int(p1.dish.price)
		q=1
		if p['id__count']==0:
				q=0
		price={}
		L=[]
		for i in x:
			z,y=int(i.quantity),int(i.dish.price)
			L.append(z*y)
			price[i.id]=z*y
		tot=sum(i for i in L)
		print(L)
		print(price)
		print(tot)
		zipped_list=zip(x,L)

		
		#print(zipped_list[0])
		
		data2=serialize('json',x)
		print(type(data2))
		
		data1={'tot':tot,'price':sibbling}
		print(data1)

		


		return JsonResponse(data1)
		#return JsonResponse( {'status': 'success'})
		
		return render(request,'cart_and_orders/cartupdate.html',{'x':x,'price':sibbling,'tot':tot,'q':q})
	#return render(request,'cart_and_orders/cartupdate.html',{'x':zipped_list,'tot':tot,'p':p})

def delete_element(request):
	cartid=request.GET.get('cartid')
	cart=Cart.objects.get(Q(user_id=request.user.id) & Q(id=cartid))
	cart.delete()
	x=(Cart.objects.filter(Q(user_id=request.user.id)).order_by('id'))

	L=[]
	for i in x:
		z,y=int(i.quantity),int(i.dish.price)
		L.append(z*y)
	print(L)
	tot=sum(i for i in L)
	data={'tot':tot}
	if request.is_ajax():
		return JsonResponse(data)
	return HttpResponseRedirect(reverse('cart'))



	
