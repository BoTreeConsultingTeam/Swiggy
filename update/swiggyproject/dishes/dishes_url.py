from dishes import views
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns=[

	
	path('adddish',views.DishAdd.as_view(),name='add_dish'),

	]

	