from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from city_and_state.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
class CustomUserCreationForm(UserCreationForm):

	 class Meta(UserCreationForm):
	 	model = CustomUser
	 	fields=('username','first_name','last_name','password1','password2','email','contact','state','city','address','pincode')

	 	def __init__(self, *args, **kwargs):
	 		 super().__init__(*args, **kwargs)
	 		 self.fields['city'].queryset = City.objects.none()


class CustomUserChangeForm(UserChangeForm):
	 model = CustomUser
	 fields='__all__'


class CustomUserCreationForm1(forms.ModelForm):
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'span11'}))
	password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'span11'}))
	state=forms.ModelChoiceField(queryset=State.objects.all())
	city=forms.ModelChoiceField(queryset=City.objects.none())
	address=forms.CharField( widget=forms.Textarea )

	def clean_password2(self):
		cd = self.cleaned_data
		
		if cd['password2'] != cd['password1']:
			raise ValidationError("Password don't match")

		return cd['password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['city'].queryset = City.objects.none()
		if 'state' in self.data:
			self.fields['city'].queryset = City.objects.filter(state_id=self.data['state'])

	def save(self, commit=True):
		user=super(CustomUserCreationForm1,self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user 

	class Meta:
		model=CustomUser
		fields=('username','first_name','last_name','email','contact','state','city','address','pincode')
		
		widgets={
		'first_name': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'last_name': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'username': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'email': forms.EmailInput(attrs={'class': 'span11', 'required': True}),
		'contact': forms.TextInput(attrs={'id': 'mask-phoneInt', 'class': 'span8 mask text','required': True}),
		'ownnershipstatus':forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
	
	#'state': forms.ModelChoiceField(queryset=State.objects.all()),
		#'password':forms.CharField(widget=forms.PasswordInput(attrs={'class': 'span11'})),
		#'password2':forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'span11'}))
		}
'''
class CustomUserAdmin(UserAdmin):

	add_form=CustomUserCreationForm1
	list_display=('username','first_name','last_name','email','contact','state','city','address','pincode')
	fieldsets = (
        (None, {'fields': ('username','first_name','last_name','email','contact','state','city','address','pincode')}),
        )
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','email','contact','state','city','address','pincode', 'is_superuser', 'is_staff', 'is_active')}
            ),
        )	
	filter_horizontal=()
	admin.site.register(CustomUserCreationForm1,CustomUserAdmin)'''