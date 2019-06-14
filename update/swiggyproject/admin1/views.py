from django.shortcuts import render
from users.models import  *
from city_and_state.models import *
from homepage.models import *
from restaurant.models import *
from cart_and_orders.models import *
from dishes.models import *
from django import forms
from django.views import View,generic
from django.conf import settings
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView,DeleteView
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
from .models import *
from .admin_forms import RestaurantForm1
from dishes.dishes_form import *
# Create your views here.
from .admin_forms import CustomUserUpdateForm
from django.db.models import Q
from django.db.models import *

class Index(View):
	def get(self,request):
		return render(request, 'admin/index1.html')

class AdminUsers(ListView):
	template_name = 'admin/users.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		return CustomUser.objects.all()

class AdminUsersUpdate(UpdateView):
	model=CustomUser
	form_class=CustomUserUpdateForm
	template_name='admin/userupdate.html'
	success_url='/admin1/adminusers'

def load_cities(request):
	print('hi')
	state_id=request.GET.get('state')
	cities=City.objects.filter(state_id=state_id).order_by('cityname')
	print(cities)
	return render(request, 'homepage/city_dropdown_list_options.html', {'cities': cities})

class AdminUserDelete(DeleteView):
	model = CustomUser
	template_name = 'admin/userdelete.html'
	success_url = '/admin1/adminusers'	

class AdminRestaurant(ListView):
	template_name = 'admin/restaurant.html'
	context_object_name = 'user_list'

	
	def get_queryset(self):
		return Restaurant.objects.all()

class AdminRestaurantUpdate(UpdateView):
	model=Restaurant
	form_class=RestaurantForm1
	template_name='admin/restaurantupdate.html'
	success_url='/admin1/adminrestaurant'

class AdminRestaurantDelete(DeleteView):
	model = Restaurant
	template_name = 'admin/restaurantdelete.html'
	success_url = '/admin1/adminrestaurant'	

class AdminApproval(View):
	def get(self,request):
		
			#form=CustomUser.objects.filter(~Q(ownnershipstatus='normaluser') & ~Q(ownnershipstatus=None))
		form=Restaurant.objects.filter(flag='0')
		print(form)
		return render(request, 'admin/approval.html', {'form': form})

class AdminApproval1(TemplateView):

	template_name= 'admin/approval.html'



	def get_context_data(self, **kwargs):
		#print(self.objects.pk)
		user = Restaurant.objects.filter(id=kwargs['pk'])
		print(user)
		return user
		print('hi',user)
		form1=CustomUser.objects.filter(ownnershipstatus='applied')
		#return {'form' : form1}


	def dispatch(self, request, *args, **kwargs):

		user = self.get_context_data( **kwargs)
		CustomUser.objects.filter(id=user[0].user_id).update(ownnershipstatus='approved')
		Restaurant.objects.filter(id=user[0].id).update(flag='1')
		#y=Restaurant.objects.all()
		x=len(Restaurant.objects.filter(Q(user_id=user[0].user_id) & Q(flag='1')))
		print(x)
		#z=Restaurant.objects.filter(flag=1).aggregate(Count('user_id'))
		#a=z['user_id__count']
		CustomUser.objects.filter(id=user[0].user_id).update(count=x)

		return redirect('approval')

class AdminApproval2(TemplateView):

	template_name= 'admin/approval.html'



	def get_context_data(self, **kwargs):
		#print(self.objects.pk)
		user = Restaurant.objects.filter(id=kwargs['pk'])
		print(user)
		return user
		print('hi',user)
		form1=CustomUser.objects.filter(ownnershipstatus='applied')


	def dispatch(self, request, *args, **kwargs):

		user = self.get_context_data( **kwargs)

		if CustomUser.objects.filter(Q(id=user[0].user_id) &  ~Q(count=0)):
			CustomUser.objects.filter(id=user[0].user_id).update(ownnershipstatus='approved')
		else:
			CustomUser.objects.filter(id=user[0].user_id).update(ownnershipstatus='normaluser')
		Restaurant.objects.filter(id=user[0].id).update(flag='2')
		return redirect('approval')

class AdminDish(ListView):
	template_name = 'admin/dishes.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		return Dishes.objects.all()

class AdminDishUpdate(UpdateView):
	
	model=Dishes
	form_class=DishForm
	template_name='admin/dishupdate.html'
	print('hello')
	success_url='/admin1/admindish'
	#success_url = '/admin1/adminrestaurant'
	
class AdminDishDelete(DeleteView):
	model = Dishes
	template_name = 'admin/dishdelete.html'
	success_url = '/admin1/admindish'	


class AdminCart(ListView):
	template_name = 'admin/cart.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		return Cart.objects.all()

class AdminCartUpdate(UpdateView):
	model=Cart
	fields='__all__'
	template_name='admin/cartupdate.html'
	success_url='/admin1/admincart'

class AdminCartDelete(DeleteView):
	model = Cart
	template_name = 'admin/cartdelete.html'
	success_url = '/admin1/admincart'

class AdminOrder(ListView):
	template_name = 'admin/order.html'
	context_object_name = 'order_list'
	
	def get_queryset(self):
		return OrdersItems.objects.all()

class AdminOrderUpdate(UpdateView):
	model=OrdersItems
	fields='__all__'
	template_name='admin/orderupdate.html'
	success_url='/admin1/adminorder'

class AdminOrderDelete(DeleteView):
	model = OrdersItems
	template_name = 'admin/orderdelete.html'
	success_url = '/admin1/adminorder'
	

	
'''
class UserListView(LoginRequiredMixin,generic.ListView):
	login_url = '/accounts/login/'
	template_name = 'user/userlistview.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		print(CustomUser.objects.all())
		return CustomUser.objects.all()'''