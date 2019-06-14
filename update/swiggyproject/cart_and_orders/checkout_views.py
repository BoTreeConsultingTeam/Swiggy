from django.shortcuts import render,redirect
from django.conf import settings 
from django.views import View,generic
from .models import *
from dishes.models import *
from users.models import CustomUser
from cart_and_orders.models import *
from django.db.models import Q
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView
import stripe

class Checkout(View):
	def get(self,request):
		user=request.user.id
		cart=Cart.objects.filter(user_id=user)
		L,X=[],[]
		for i in cart:
			z,y=int(i.quantity),int(i.dish.price)
			X.append(z*y)
			L.append(((z*y)+(z*y*5/100)))
		tot_tax=sum(i for i in L)
		tot=sum(i for i in X)
		print(cart)
		zipped_list=zip(cart,L)
		return render(request,'cart_and_orders/checkout.html',{ 'data':zipped_list,'tot_tax':tot_tax,'tot':tot})


class OrdersView(View):
	def get(self,request):
		user=request.user.id
		cart=Cart.objects.filter(user_id=user)
		person=CustomUser.objects.filter(id=user)
		price1=[]
		for i in cart:
			z,y=int(i.quantity),int(i.dish.price)
			price1.append(((z*y)+(z*y*5/100)))
		tot_tax=sum(i for i in price1)
		tot_tax_dol=(tot_tax/70)*100
		print(tot_tax_dol)
		zipped_list=zip(cart,price1)

		

		return render(request,'cart_and_orders/order.html',{'person':person, 'data':zipped_list,'tot_tax':tot_tax,'tot_tax_dol':tot_tax_dol})

	def post(self,request):
		stripe.api_key='sk_test_ixsGVmowuzrZVGHne7fNfq4h00zViDri9W'
		

		user=request.user.id
		deliveryaddress=request.POST['deliveryaddress']	
		cart=Cart.objects.filter(user_id=user)
		#print('cart=',cart.values())
		res_id=cart[0].restaurant_id
		print('res_id=',res_id)
		price1,X=[],[]

		for i in cart:
			z,y=int(i.quantity),int(i.dish.price)
			price1.append(((z*y)+(z*y*5/100)))
			X.append(z*y)

		tot=sum(i for i in X)	
		tot_tax=sum(i for i in price1)
		tot_tax_dol=int((tot_tax/70)*100)
		print(tot_tax_dol)
		charge = stripe.Charge.create(
		amount=tot_tax_dol,
		currency='usd',
		description='A Django charge',
		source=request.POST['stripeToken']
		)
		print(request.POST['stripeToken'])

		
		
		orders=Orders.objects.create(
				user_id=user,
				restaurant_id=res_id,
				totalpricetax=str(tot_tax),
				orderstatus='orderplaced'
				)
		print('order_id=',orders.id)
		#print(orders)
		#print('orders=',Orders.objects.filter(id=orders.id).values())
		address=DeliveryAddress.objects.create(orders=orders ,deliveryaddress=deliveryaddress)
		for item in cart:
				
			orderitems=OrdersItems.objects.create(

						orders=orders,
						quantity=item.quantity,
						totalprice=int(item.dish.price) * int(item.quantity),
						dish_id=item.dish.id

					) 
			#print('orderitems=',OrdersItems.objects.filter(id=orderitems.id).values()) 
			cart.delete()
			#print('After Deletion from Cart ,count=',cart.count())

		'''def get_context_data(self, **kwargs): # new
			context = super().get_context_data(**kwargs)
			print(settings.STRIPE_PUBLISHABLE_KEY)
			context['key'] = settings.STRIPE_PUBLIC_KEY
			return context '''
		return redirect('index')


'''def charge(request): # new
	if request.method == 'POST':

	return redirect('index')'''

