from django.test import TestCase,Client
from .models import *
from django.urls import reverse
from django.db.models import Count
from cart_and_orders.models import *
class CartAndOrdersModelTest(TestCase):
	fixtures=['cart_and_orders/fixtures/cartorders.json']

	@classmethod
	def setUpClass(cls):
		super(CartAndOrdersModelTest, cls).setUpClass()
		
	def test_cart_quantity(self):
		cart_object=Cart.objects.get(id=149)
		self.assertEquals(int(cart_object.quantity),3)

	def test_order_orderstatus(self):
		order_object=Orders.objects.get(id=29)
		self.assertEquals(order_object.orderstatus,'orderplaced')

	def test_orderitems_totalprice(self):
		orderitems_object=OrdersItems.objects.get(id=27)
		self.assertEquals(int(orderitems_object.totalprice),600)

class CartAndOrder_viewsTest(TestCase):
	fixtures=['cart_and_orders/fixtures/cartorders.json']

	@classmethod
	def setUpClass(cls):
		super(CartAndOrder_viewsTest, cls).setUpClass()

	def test_addtocart_url(self):
		client=Client()
		response=client.get('/cart_and_orders/cart',{'id':'16'})
		self.assertEquals(response.status_code,200)

	def test_orderitem_verify_total_price(self):
		orderitems_object=OrdersItems.objects.get(id=27)
		self.assertEquals(int(orderitems_object.quantity)*int(orderitems_object.dish.price),int(orderitems_object.totalprice))

	def test_cart_status_code(self):
		client=Client()
		response=client.get('/cart_and_orders/cart')
		self.assertEquals(response.status_code,200)

class CartAndOrder_views_Ajax_test(TestCase):
	fixtures=['cart_and_orders/fixtures/cartorders.json']

	@classmethod
	def setUpClass(cls):
		super(CartAndOrder_views_Ajax_test, cls).setUpClass()

	def test_pluscart(self):
		cart_object=Cart.objects.get(id=149)
		client = Client()
		data={'dataid':cart_object.id,'quantityinput':15,'btnid':'+'}
		client.login(username=cart_object.user.username,password='swiggy123')
		response=client.get(reverse('cartupdate'),data, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
		print(response.content)
		self.assertEquals(response.status_code,200)
		self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'tot': 5100, 'price': 4800}
        )

	def test_delete_element(self):
		cart_object=Cart.objects.get(id=149)
		client = Client()
		data={'cartid':cart_object.id}
		client.login(username=cart_object.user.username,password='swiggy123')	
		response=client.get(reverse('cartdelete'),data, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
		self.assertEquals(response.status_code,200)
		print('jsonresponse=',str(response.content, encoding='utf8'))
		self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'tot': 300}
        )

class CartAndOrder_myordersviewsTest(TestCase):
	fixtures=['cart_and_orders/fixtures/cartorders.json']

	@classmethod
	def setUpClass(cls):
		super(CartAndOrder_myordersviewsTest, cls).setUpClass()

	def test_MyOrdersViewTest(self):
		order_object=Orders.objects.get(id=29)
		client = Client()
		client.login(username=order_object.user.username,password='swiggy123')	
		response=client.get(reverse('myorder'))
		self.assertEquals(response.status_code,200)

	def test_MyOrdersDetailsViewTest(self):
		client=Client()
		response=client.get(reverse('myorderdetails'),{'id':16})
		self.assertEquals(response.status_code,200)

	def test_RestaurantRecieveOrderViewTest(self):
		restaurant_object=Restaurant.objects.get(id=27)
		client = Client()
		client.login(username=restaurant_object.user.username,password='swiggy123')	
		response=client.get(reverse('recieveorderdetails'))
		self.assertEquals(response.status_code,200)

	def test_OrderStatusUpdateViewTest(self):
		client = Client()
		order_object=Orders.objects.get(id=29)
		client.login(username=order_object.user.username,password='swiggy123')
		data={'orderid':order_object.id,'status1':order_object.orderstatus}	
		response=client.get(reverse('orderstatusupdate'),data, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
		self.assertEquals(response.status_code,200)

	def test_ChangeRestaurantOrderviewTest(self):
		restaurant_object=Restaurant.objects.get(id=27)
		client = Client()
		client.login(username=restaurant_object.user.username,password='swiggy123')
		data={'restaurantid':restaurant_object.id}	
		response=client.get(reverse('changerestaurantorder'),data,**{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
		self.assertEquals(response.status_code,200)

class CartAndOrder_CheckoutViewsTest(TestCase):
	fixtures=['cart_and_orders/fixtures/cartorders.json']

	@classmethod
	def setUpClass(cls):
		super(CartAndOrder_CheckoutViewsTest, cls).setUpClass()

	def test_Checkout(self):
		cart_object=Cart.objects.get(id=149)

		client = Client()
		client.login(username=cart_object.user.username,password='swiggy123')
		response=client.get(reverse('checkout'))
		self.assertEquals(response.status_code,200)

	def test_OrdersView_status_code_get(self):
		cart_object=Cart.objects.filter(user_id=20)
		print('cart=',cart_object)	

		client = Client()
		client.login(username=cart_object[0].user.username,password='swiggy123')
		response=client.get(reverse('order'))
		self.assertEquals(response.status_code,200)

	'''def test_OrdersView_status_code_post(self):
		cart_object=Cart.objects.filter(user_id=20)
		#print(cart_object)
		#print('Intitally Count of cart ,count=',cart_object1)
		self.assertEquals(cart_object.count(),2)
		print('orders(previous latest)=',Orders.objects.filter(user_id=20).latest('id'))
		#print('username=',cart_object[0].user.username)
		client = Client()
		client.login(username=cart_object[0].user.username,password='swiggy123')
		data={'deliveryaddress':'asdf'}
		response=client.post(reverse('order'),data)
		orders=Orders.objects.filter(user_id=20).latest('id')
		print('orders(latest)=',orders)
		#print(cart_object)
		#print('After Deletion from Cart ,count=',cart_object.count())
		self.assertEquals(cart_object.count(),0)
		#print(response)
		self.assertEquals(response.status_code,302)'''