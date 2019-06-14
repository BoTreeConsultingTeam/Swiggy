from django.test import TestCase,Client
from .models import Restaurant
from django.urls import reverse
from restaurant.restaurant_form import *
class RestaurantModelTest(TestCase):

	fixtures=['restaurant/fixtures/restaurant.json']

	@classmethod
	def setUpClass(cls):
		super(RestaurantModelTest, cls).setUpClass()
		print(Restaurant.objects.all())

	def test_restaurantname(self):
		restaurant_object=Restaurant.objects.get(id=27)
		self.assertEquals(restaurant_object.restaurantname,'Honest')

	def test_city(self):
		restaurant_object=Restaurant.objects.get(id=27)
		print(restaurant_object.city.cityname)
		self.assertEquals(restaurant_object.city.cityname,'ahmedabad')	

class RestaurantViewsTest(TestCase):

	fixtures=['restaurant/fixtures/restaurant.json']

	@classmethod
	def setUpClass(cls):
		super(RestaurantViewsTest, cls).setUpClass()
		print(Restaurant.objects.all())

	def test_status_code_get(self):
		c = Client()
		c.login(username='binoy',password='swiggy123')
		response = c.get('/restaurant/signup')
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'restaurant/resaturantpartner.html')

	def test_status_code_post(self):
		data={
		"ownername": "Binoy",
		"restaurantname": "Chinese",
		"bank_account_no": "78645256656",
		"state": 1,
		"city": 7,
		"address": "sec 3",
		"img": "images/chinese5.jpeg",
		"user": 20,
		}

		url=reverse('rsignup')
		client=Client()
		client.login(username='binoy',password='swiggy123')
		response = client.post(url, data)
		self.assertEquals(response.status_code, 302)
		self.assertURLEqual(response.url,"/index/")	


class RestaurantFormsTest(TestCase):

	fixtures=['restaurant/fixtures/restaurant.json']

	@classmethod
	def setUpClass(cls):
		super(RestaurantFormsTest, cls).setUpClass()
		print(Restaurant.objects.all())

	def test_restaurant_form(self):
		data1 = {
		"ownername": "",
		"restaurantname": "Chinese",
		"bank_account_no": "78645256656",
		"state": 1,
		"city": 7,
		"address": "sec 3",
		"img": "images/chinese5.jpeg",
		"user": 20,
		}
 		
		url=reverse('rsignup')
		client=Client()
		client.login(username='binoy',password='swiggy123')
		response = client.post(url, data1,follow=True)
		form = RestaurantForm(data = data1)
		if form.is_valid():
			self.assertEquals(response.status_code,200 )
			p=form.is_valid()
			print(p)
		else:
			#print(form.errors)
			self.assertTrue(form.errors)
		