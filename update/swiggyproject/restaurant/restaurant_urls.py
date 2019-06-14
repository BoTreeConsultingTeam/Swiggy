from restaurant import views
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
 	
urlpatterns=[

	path('signup',views.Restaurantregistration.as_view(),name='rsignup'),
	path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
	
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 