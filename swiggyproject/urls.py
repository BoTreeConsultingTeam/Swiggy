"""swiggyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('homepage.homepage_urls')),
    path('users',include('users.users_url')),
    path('admin1',include('admin1.admin_urls')),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    path('accounts/', include('django.contrib.auth.urls') ,name='login'),
    path('restaurant/',include('restaurant.restaurant_urls')),
    path('dishes/',include('dishes.dishes_url')),
    path('cart_and_orders/',include('cart_and_orders.cart_and_orders_urls'))
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 