from django.shortcuts import render
from django import forms
from django.views import View,generic
from django.conf import settings
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView
from users.user_forms import CustomUserCreationForm1,CustomUserCreationForm
from city_and_state.models import *
from .models import *
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
# Create your views here.

class Signup(View):
	def get(self,request):
		form = CustomUserCreationForm1
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