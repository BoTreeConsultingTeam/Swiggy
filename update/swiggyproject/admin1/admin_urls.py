from admin1 import views
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns=[

	path('/index',views.Index.as_view(),name='adminindex'),
	path('/adminusers',views.AdminUsers.as_view(),name='adminusers'),
	path('/approval/',views.AdminApproval.as_view(),name='approval'),
	path('/approval1/(?P<pk>[\w-])',views.AdminApproval1.as_view(),name='approval1'),
	path('/approval2/(?P<pk>[\w-])',views.AdminApproval2.as_view(),name='approval2'),
	path('/adminrestaurant',views.AdminRestaurant.as_view(),name='adminrestaurant'),
	path('/admindish',views.AdminDish.as_view(),name='admindish'),
	path('/admincart',views.AdminCart.as_view(),name='admincart'),
	path('/adminorder',views.AdminOrder.as_view(),name='adminorder'),
	

	path('/adminuserdelete/(?P<pk>[\w-]+)',views.AdminUserDelete.as_view(),name='adminuserdelete'),
	path('/adminrestaurnatdelete/(?P<pk>[\w-]+)',views.AdminRestaurantDelete.as_view(),name='adminrestaurantdelete'),
	path('/admindishdelete/(?P<pk>[\w-]+)',views.AdminDishDelete.as_view(),name='admindishdelete'),
	path('/adminorderdelete/(?P<pk>[\w-]+)',views.AdminOrderDelete.as_view(),name='adminorderdelete'),
	path('/admincartdelete/(?P<pk>[\w-]+)',views.AdminCartDelete.as_view(),name='admincartdelete'),
	

	path('/adminuserupdate/(?P<pk>[\w-]+)',views.AdminUsersUpdate.as_view(),name='adminusersupdate'),
	path('/adminrestaurantupdate/(?P<pk>[\w-]+)',views.AdminRestaurantUpdate.as_view(),name='adminrestaurantupdate'),
	path('/admindishupdate/(?P<pk>[\w-]+)',views.AdminDishUpdate.as_view(),name='admindishupdate'),
	path('/adminorderupdate/(?P<pk>[\w-]+)',views.AdminOrderUpdate.as_view(),name='adminorderupdate'),
	path('/admincartupdate/(?P<pk>[\w-]+)',views.AdminCartUpdate.as_view(),name='admincartupdate'),
	
	
]