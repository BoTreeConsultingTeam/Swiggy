from django.shortcuts import render
from city_and_state.models import *
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

class Restaurantregistration(LoginRequiredMixin,View):
	def get(self,request):
		form = RestaurantForm()
		print('resid=',request.user.id)
		return render(request, 'restaurant/resaturantpartner.html', {'form': form})
		#success_url="home"
	def post(self,request):
		if request.method == 'POST':
			form = RestaurantForm(request.POST, request.FILES)


			
			#print(form,'hi')
			if form.is_valid():
				object=form.save(commit=False)
				object.user_id=request.user.id
				object.save()
				


			print(request.user.id)
			x=CustomUser.objects.filter(Q(id=request.user.id) & Q(count=0))
			if x:
				CustomUser.objects.filter(id=request.user.id).update(ownnershipstatus='applied')	
			return redirect('index')
			#success_url="home"
		else:
			form = RestaurantForm()
		return render(request, 'restaurant/resaturantpartner.html', {'form': form})

def load_cities(request):
	print('hi')
	state_id=request.GET.get('state')
	cities=City.objects.filter(state_id=state_id).order_by('cityname')
	print(cities)
	return render(request, 'homepage/city_dropdown_list_options.html', {'cities': cities})