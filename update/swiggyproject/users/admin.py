from django.contrib import admin
from users.models import *
from city_and_state.models import *
from users.user_forms import *
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
	fields=('username','first_name','last_name','password1','password2','email','contact','state','city','address','pincode','ownnershipstatus')
	form=CustomUserCreationForm1
	list_display=('username','first_name','last_name','email','contact','state','city','address','pincode','ownnershipstatus')
	#search_fields=('username','first_name','last_name','email','contact','state','city','address','pincode','ownnershipstatus')

admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
