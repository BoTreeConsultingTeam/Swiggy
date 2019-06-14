from django.shortcuts import render
from city_and_state.models import *
from users.models import *
# Create your views here.
from django.shortcuts import render
from django import forms
from django.views import View,generic
from django.conf import settings
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView
#from users.user_forms import CustomUserCreationForm1,CustomUserCreationForm

from .models import *
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
from restaurant.restaurant_form import *
from django.contrib.auth.mixins import *
from django.db.models import Q
from dishes.dishes_form import *


class RestaurantRequiredredMixin(object):
	
	def dispatch(self,request,*args,**kwargs):
		x=CustomUser.objects.get(id=request.user.id)
		print(x)
		if int(x.count)<1:
			#raise PermissionsDenied
			return redirect('index')
		
		return super(RestaurantRequiredredMixin,self).\
				dispatch(request,*args,**kwargs)

class DishAdd(LoginRequiredMixin,RestaurantRequiredredMixin,CreateView):
	form_class=DishForm
	template_name='dishes/add_dishes.html'
	success_url='/index'

	def get_form_kwargs(self):
		kwargs = super(DishAdd, self).get_form_kwargs()

		if self.request.method == 'GET':
			kwargs.update({
				'user': self.request.user.id,
			})
		return kwargs