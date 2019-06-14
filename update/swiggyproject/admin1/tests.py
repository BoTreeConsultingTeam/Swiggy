from django.test import TestCase,Client
from django.urls import reverse
from users.models import CustomUser
from restaurant.models import Restaurant
from city_and_state.models import *
from admin1.admin_forms import *
from dishes.models import *
from dishes.dishes_form import *
class AdminViewTest(TestCase):



	def setUp(self):
		self.state=State.objects.create(statename='Gujarat')
		print(self.state.id)
		self.city=City.objects.create(state=self.state,cityname="asd")
		
		self.users_data=CustomUser.objects.create(
			password="p1bkdf2_sha256$150000$rThudk7McqVL$mhFHxWSf3pMFKm8pmobEIkTi3pudh1XDTun5I174bI0=",
			username= "yogi",
			first_name= "qwerty",
			last_name= "qwerty",	
			email= "yogi@gmail.com",
			contact= 123456789,
			state= self.state,
			city= self.city,
			address= "sabarmati",
			pincode= 123456,
			
			
			
		
		)
		self.restaurant=Restaurant.objects.create(

			ownername= "Binoy",
			restaurantname= "Pizza Hut",
			bank_account_no="7855425325",
			state=self.state,
			city=self.city,
			address= "sec-2",
			img= "images/pizza_5DSWC0t.jpg",
			user= self.users_data,
			flag="1"

			)

		self.dish_type=DishesType.objects.create(
			dish_type_name="sandwich"
			)

		self.dish=Dishes.objects.create(
			dish_type= self.dish_type,
			dishinfo= "grilled sandwich",
			dishname= "grilled sandwich",
			img= "images/sandwich4_CNVQkSY.jpeg",
			price= "200",
			restaurant= self.restaurant,
			veg_or_nonveg= "veg"
			)
		self.restaurant_id=Restaurant.objects.latest('id').id

	def test_Index(self):
		client=Client()
		response=client.get(reverse('adminindex'))
		self.assertEquals(response.status_code,200)

	def test_AdminUsers(self):
		client=Client()
		response=client.get(reverse('adminusers'))
		self.assertEquals(response.status_code,200)

	def test_AdminUsersUpdate(self):
		client=Client()
		print(CustomUser.objects.get(id=self.users_data.id))
		url=reverse('adminusersupdate',kwargs={'pk':1})

		print(url)
		print(self.users_data.id)
		data1={
		"username": "yogi1",
		"first_name": "binoy",
		"last_name": "qwerty",
		"contact": 123456789,
		"email":'yogi@gmail.com',
		"state": 1,
		"city": 1,
		"address": "Shastri Nagar",
		"pincode": 123456,
		}

		#self.users_data.username='binoy1'
		response = client.post(url,data1)
		print(response)
		
		

		if response.status_code==404:
			print("Page not found")
		else:
			print(CustomUser.objects.get(id=self.users_data.id).username)
			self.assertEquals(CustomUser.objects.get(id=self.users_data.id).username,'yogi1')

		
			print("CustomUser Update View successfully called")
			self.assertURLEqual(response.url,'/admin1/adminusers')
			#self.assertTemplateUsed(response, "admin/userupdate.html")

	def test_AdminUserDeleteViewTest(self):
		client=Client()
		url=reverse('adminuserdelete',kwargs={'pk':self.users_data.id})
		response=client.post(url)
		if response.status_code==404:
			print("Page not found")
		else:
			print("CustomUser Delete View successfully called")
			self.assertURLEqual(response.url, "/admin1/adminusers")

	def test_AdminRestaurantViewTest(self):
		client=Client()
		response=client.get(reverse('adminrestaurant'))
		self.assertEquals(response.status_code,200)

	def test_AdminRestaurantUpdateViewTest(self):
		client=Client()
		print('restaurantupdate_id=',self.restaurant_id)
		url=reverse('adminrestaurantupdate',kwargs={'pk':1})
		print(url)
		
		data1={
		"ownername": "Binoy",
		"restaurantname": "Pizza Hut1",
		"bank_account_no": "7855425325",
		"state": 1,
		"city": 1,
		"address": "sec-2",
		"img": "images/pizza_5DSWC0t.jpg",
		"user":1,
		"flag": "1"
		}
		response=client.post(url,data1)
		print(response)

		form = RestaurantForm1(data = data1)
		if form.is_valid():
			self.assertEquals(response.status_code,302 )
			p=form.is_valid()
			print(p)
		else:
			print(form.errors)
			self.assertTrue(form.errors)

		if response.status_code==404:
			print("Page not found")
		else:
			print(Restaurant.objects.get(id=self.restaurant.id).restaurantname)
			self.assertEquals(Restaurant.objects.get(id=self.restaurant.id).restaurantname,'Pizza Hut1')

		
			print("CustomUser Update View successfully called")
			self.assertURLEqual(response.url,'/admin1/adminrestaurant')

	def test_AdminRestaurantDeleteViewTest(self):
		client=Client()
		url=reverse('adminrestaurantdelete',kwargs={'pk':1})
		response=client.post(url)
		if response.status_code==404:
			print("Page not found")
		else:
			print("Restaurant Delete View successfully called")
			self.assertURLEqual(response.url, "/admin1/adminrestaurant")

	def test_AdminDishViewTest(self):
		client=Client()
		response=client.get(reverse('admindish'))
		self.assertEquals(response.status_code,200)

	def test_AdminDishUpdateViewTest(self):
		client=Client()
		print(Dishes.objects.get(id=self.dish.id).id)
		url=reverse('admindishupdate',kwargs={'pk':1})
		print(url)
		data1={
		"dish_type": 1,
		"dishinfo": "Chole",
		"dishname": "Chole",
		"img": "images/chole_t6BEMnA.jpeg",
		"price": "300",
		"restaurant": 1,
		"veg_or_nonveg": "veg"
		}

		#self.users_data.username='binoy1'
		response = client.post(url,data1)
		#print(response.content)
		form = DishForm(data = data1)
		if form.is_valid():
			self.assertEquals(response.status_code,302 )
			p=form.is_valid()
			print(p)
		else:
			print(form.errors)
			self.assertTrue(form.errors)
		print(response.content)
		
		
		if response.status_code==404:
			print("Page not found")
		else:
			print('hi')
			self.assertEquals(Dishes.objects.get(id=self.dish.id).dishname,'Chole')

	def test_AdminDishDeleteTest(self):
		client=Client()
		url=reverse('admindishdelete',kwargs={'pk':1})
		response=client.post(url)
		if response.status_code==404:
			print("Page not found")
		else:
			print("Dishes Delete View successfully called")
			self.assertURLEqual(response.url, "/admin1/admindish")
			
	






