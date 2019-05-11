from django.shortcuts import render
from django.views import View,generic
from .models import *
from dishes.models import *
from django.db.models import Q
# Create your views here.
class AddToCart(View):
	def get(self,request):
		id=request.GET.get('id')
		print('id=',id)

		a=Dishes.objects.filter(id=id)
		y=request.user.id
		if id!=None:
			b=Cart.objects.create(quantity=1,dish_id=id,restaurant_id=a[0].restaurant.id,user_id=y)
		x=Cart.objects.filter(Q(user_id=y))
		
		return render(request,'cart_and_orders/cart.html',{'x':x})