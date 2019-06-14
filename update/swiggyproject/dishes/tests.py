from django.test import TestCase,Client
from .models import *
from django.urls import reverse
from dishes.dishes_form import *
# Create your tests here.

class DishesModelTest(TestCase):
	fixtures=['dishes/fixtures/dishes.json']

	@classmethod
	def setUpClass(cls):
		super(DishesModelTest, cls).setUpClass()
		print(Dishes.objects.all())

	def test_restaurantname(self):
		dishes_object=Dishes.objects.get(id=11)
		self.assertEquals(dishes_object.restaurant.restaurantname,'Honest')

	def test_city(self):
		dishes_object=Dishes.objects.get(id=11)
		self.assertEquals(dishes_object.dishname,'Chole')	

class DishesTypeModelTest(TestCase):
	fixtures=['dishes/fixtures/dishes.json']

	@classmethod
	def setUpClass(cls):
		super(DishesTypeModelTest, cls).setUpClass()
		print(DishesType.objects.all())

	def test_dishtypename(self):
		dishes_type_object=DishesType.objects.get(id=5)
		self.assertEquals(dishes_type_object.dish_type_name,'Sandwich')

class DishesViewTest(TestCase):
	fixtures=['dishes/fixtures/dishes.json']

	@classmethod
	def setUpClass(cls):
		super(DishesViewTest, cls).setUpClass()
		print(Dishes.objects.all())

	def test_status_code_get(self):
		c=Client()
		c.login(username='binoy',password='swiggy123')
		response = c.get('/dishes/adddish')
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'dishes/add_dishes.html')

	def test_status_code_post(self):
		data={

		"dish_type": 4,
		"dishinfo": "panipuri",
		"dishname": "panipuri",
		"img": "images/panipuri6_52mdm5b.jpeg",
		"price": "30",
		"restaurant": 27,
		"veg_or_nonveg": "veg"
		}
		url=reverse('add_dish')
		c=Client()
		c.login(username='binoy',password='swiggy123')
		response=c.post(url,data)
		self.assertEquals(response.status_code, 302)
		self.assertURLEqual(response.url,"/index")	

class DishesFormTest(TestCase):
	fixtures=['dishes/fixtures/dishes.json']

	@classmethod
	def setUpClass(cls):
		super(DishesFormTest, cls).setUpClass()
		print(Dishes.objects.all())

	def test_dishes_form(self):
		data={
		"dish_type": 4,
		"dishinfo": "panipuri",
		"dishname": "panipuri",
		"img": "images/panipuri6_52mdm5b.jpeg",
		"price": "30",
		"restaurant": 27,
		"veg_or_nonveg": ""
		}
		url=reverse('add_dish')
		c=Client()
		c.login(username='binoy',password='swiggy123')
		response=c.post(url,data,follow=True)
		form = DishForm(data = data)
		if form.is_valid():
			self.assertEquals(response.status_code,200 )
			p=form.is_valid()
			print(p)
		else:
			#print(form.errors)
			self.assertTrue(form.errors)



