from django.contrib import admin
from users.models import *
from city_and_state.models import *
# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.site_header='Swiggy DashBoard'

