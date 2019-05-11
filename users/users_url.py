from users import views
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
 	
urlpatterns=[

	path('/',views.Signup.as_view(),name='signup'),
	path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
	
]