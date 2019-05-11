from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from restaurant.models import Restaurant
from city_and_state.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from restaurant.restaurant_form import RestaurantForm
class CustomUserUpdateForm(forms.ModelForm):
	state=forms.ModelChoiceField(queryset=State.objects.all())
	city=forms.ModelChoiceField(queryset=City.objects.none())
	address=forms.CharField( widget=forms.Textarea )


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['city'].queryset = City.objects.none()
		if 'state' in self.data:
			self.fields['city'].queryset = City.objects.filter(state_id=self.data['state'])



	class Meta:
		model=CustomUser
		fields=('username','first_name','last_name','email','contact','state','city','address','pincode')
		
		widgets={
		'first_name': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		'last_name': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		'username': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		'email': forms.EmailInput(attrs={ 'required': True}),
		#'contact': forms.TextInput(attrs={'id': 'mask-phoneInt', 'class': 'span8 mask text','required': True}),
		'ownnershipstatus':forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		}

class RestaurantForm1(forms.ModelForm):
	state=forms.ModelChoiceField(queryset=State.objects.all())
	city=forms.ModelChoiceField(queryset=City.objects.none())
	address=forms.CharField( widget=forms.Textarea )

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['city'].queryset = City.objects.none()
		if 'state' in self.data:
			self.fields['city'].queryset = City.objects.filter(state_id=self.data['state'])

	class Meta:
		model=Restaurant
		fields='__all__'

		widgets={
		'ownername': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		'restaurantname': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		'bankaccountno': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		}