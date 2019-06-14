from django.shortcuts import render,redirect
from django import forms
from django.views import View,generic
from django.conf import settings
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView
from users.user_forms import CustomUserCreationForm1,CustomUserCreationForm
from city_and_state.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
from django.contrib import messages
# Create your views here.

class Signup(View):
	def get(self,request):
		form = CustomUserCreationForm1()
		return render(request, 'users/signup.html', {'form': form})
		#success_url="home"
	def post(self,request):
		if request.method == 'POST':
			form = CustomUserCreationForm1(request.POST)
			

			print('password=',request.POST['password1'])
			#print(form,'hi')
			if form.is_valid():
				form.save()
				
				return redirect('index')
				#success_url="home"
		else:
			form = CustomUserCreationForm1()
		return render(request, 'users/signup.html', {'form': form})

class Login_Request(View):
	def get(self,request):
		form=AuthenticationForm()
		return render(request,'registration/login.html', {'form': form})

	def post(self,request):
		print('789462')
		form=AuthenticationForm(data=request.POST)
		#print(form.is_valid)
		if form.is_valid():
			#print('form')
			#return HttpResponseRedirect(request.GET['next'])
			username=form.cleaned_data.get('username')
			print(username)
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			print('hi123')
			print(user)
			print('hi456')
			if user is not None:
				login(request,user)
				if user.is_superuser:
					return redirect('adminindex')
				else:
					return redirect('index')
					
			else:
				message.error(request,'Invalid username or password')
		else:
			#print('form Invalid')
			return render(request,'registration/login.html', {'form': form})
			
		
'''class Signup(CreateView):
	template_name='homepage/signup.html'
	form_class=	CustomUserCreationForm1	
	print(CustomUser.objects.all())
	success_url='/index' '''

def load_cities(request):
	print('hi')
	state_id=request.GET.get('state')
	cities=City.objects.filter(state_id=state_id).order_by('cityname')
	print(cities)
	return render(request, 'homepage/city_dropdown_list_options.html', {'cities': cities})