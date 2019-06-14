from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from city_and_state.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from restaurant.models import *



class RestaurantForm(forms.ModelForm):
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
		fields=('ownername','restaurantname','bank_account_no','state','city','address','img')

		widgets={
		'ownername': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'restaurantname': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'bankaccountno': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		}