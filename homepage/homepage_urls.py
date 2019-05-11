from homepage import views
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns=[

	
	path('',views.Test.as_view(),name='index'),
	path('food',views.Food.as_view(),name='food')
]