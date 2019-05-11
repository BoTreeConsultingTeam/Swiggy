from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from city_and_state.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from restaurant.models import *
from dishes.models import *


class DishForm(forms.ModelForm):
	restaurant=forms.ModelChoiceField(label='Restaurant name',queryset=Restaurant.objects.all(),empty_label='Select Your Restaurant')
	#dish_type=forms.ModelChoiceField(label='DishType',queryset=Dishes.objects.all(),empty_label='Select Your Dish')
	
	dishinfo=forms.CharField( widget=forms.Textarea )


	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(DishForm, self).__init__(*args, **kwargs)
		if user is not None:
			self.fields['restaurant'].queryset = Restaurant.objects.filter(user_id=user)

	class Meta:
		model=Dishes
		CHOICES=[('veg','male'),
         ('nonveg','female')]

		veg_or_nonveg = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
		fields=('name','date_time','weight','age','gender')
		fields='__all__'

		widgets={
		'dishname': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		'restaurantname': forms.TextInput(attrs={ 'autofocus': True, 'required': True}),
		
		}