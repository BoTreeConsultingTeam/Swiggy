from cart_and_orders import views
from cart_and_orders import checkout_views as checkviews
from cart_and_orders import myorders_views as myorderviews
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns=[

	
	path('cart',views.AddToCart.as_view(),name='cart'),
	path('cartupdate',views.pluscart,name='cartupdate'),
	path('cartdelete',views.delete_element,name='cartdelete'),
	path('checkout',checkviews.Checkout.as_view(),name='checkout'),
	path('order',checkviews.OrdersView.as_view(),name='order'),
	path('myorder',myorderviews.MyOrdersView.as_view(),name='myorder'),
	path('orderupdate',myorderviews.OrderStatusUpdate,name='orderstatusupdate'),
	path('restaurantorder',myorderviews.RestaurantRecieveOrderView.as_view(),name='restaurantorder'),
	path('restaurantorderreport',myorderviews.RestaurantOrdersReports.as_view(),name='restaurantreport'),
	path('api/restaurantorderreport/(?P<pk>[\w-])',myorderviews.RestaurantOrdersReportsAPI.as_view(),name='restaurantreportapi'),
	#path('pdfdownload',myorderviews.TestView.as_view(),name='pdf'),
	#path('graphpdf',myorderviews.GraphPdfView.as_view(),name='graphpdf'),
	path('api/restaurantreportweeklyapi/(?P<pk>[\w-])',myorderviews.RestaurantOrdersReportsWeeklyAPI.as_view(),name='restaurantreportweeklyapi'),
	#path('api/restaurantreportquaterlyapi/(?P<pk>[\w-])',myorderviews.RestaurantOrdersReportsQuaterlyAPI.as_view(),name='restaurantreportquaterlyapi'),
	#path('api/restaurantreportmonthlyapi/(?P<pk>[\w-])',myorderviews.RestaurantOrdersReportsMonthlyAPI.as_view(),name='restaurantreportmonthlyapi'),
	path('changerestaurantorder',myorderviews.changerestaurantorder,name='changerestaurantorder'),
	path('myorderdetails',myorderviews.MyOrdersDetailsView.as_view(),name='myorderdetails'),
	path('recieveorderdetails',myorderviews.RecieveOrdersDetailsView.as_view(),name='recieveorderdetails'),
	#path('pdf_xht/$',myorderviews.MyPDFView.as_view(),name='hipdf'),
	path('imgdecode',myorderviews.ImgDecode.as_view(),name='imgpdf'),

	#path('charge/', checkviews.charge, name='charge'),

	]

	