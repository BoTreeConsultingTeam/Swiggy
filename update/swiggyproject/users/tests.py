from django.test import TestCase,Client
from .models import CustomUser
from city_and_state.models import State,City
import re
import json
from django.test import Client
from django.urls import reverse
from users.user_forms import CustomUserCreationForm1,CustomUserCreationForm
# Create your tests here.
class CustomUserModelTest(TestCase):

	def setUp(self):
		self.state=State.objects.create(statename='Gujarat')
		self.city=City.objects.create(state=self.state,cityname="asd")
		self.user=CustomUser.objects.create(

			username='meet',
			email='meet@gmail.com',
			count=2,
			city=self.city,
			state=self.state,
			first_name='meet',
			last_name='parikh',
			contact=1654465194,
			address='ahmedabad',
			pincode=123456,
			password='swiggy123',

			)

		self.user1=CustomUser.objects.create(

			username='met',
			email='meet1@gmail.com',
			count=23,
			city=self.city,
			state=self.state,
			first_name='meet',
			last_name='parikh',
			contact=1654465194,
			address='ahmedabad',
			pincode=123456,
			password='swiggy123',
			)


	def test_csrf(self):
		url = reverse('login')
		client=Client()
		client.login(username='binoy',password='swiggy123')
		response =client.post(url)
		print(response.context.get('username'))
		print(response)
		self.assertContains(response, 'csrfmiddlewaretoken')

	def test_count(self):
		#print(type(self.user.count()))
		self.assertFalse(self.user.count==1)
		self.assertFalse(self.user1.count==1)


	def test_count1(self):
		self.assertEquals(self.user.count,2)
		self.assertEquals(self.user1.count,23)


	def test_password(self):
		self.assertEquals(self.user.password,'swiggy123')	
		self.assertEquals(self.user1.password,'swiggy123')	


	def test_validemailaddress(self):
		x="[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
		self.assertTrue(re.match(x, self.user.email))
		self.assertTrue(re.match(x, self.user1.email))


class LoginAndSignupUrlTest(TestCase):

	def test_login(self):
		c = Client()
		response = c.post('/login/', {'username': 'meet', 'password': 'swiggy123'})
		response1 = c.post('/login/', {'username': 'met', 'password': 'swiggy123'})
		#response = c.get('/restaurant/signup', follow=True)
		self.assertEquals(response.status_code,200)
		print(response.context.get('widget')['value'])
		self.assertEquals(response1.status_code,200)


	def test_signup(self):
		c = Client()
		response = c.get('/users/')
		self.assertEquals(response.status_code,200)

class UserTestCaseFixture(TestCase):

	fixtures=['users/fixtures/users.json']

	@classmethod
	def setUpClass(cls):
		super(UserTestCaseFixture, cls).setUpClass()
		#self.user= CustomUser.objects.create()
		#import code; code.interact(local=dict(globals(), **locals()))
		print(CustomUser.objects.all())

	def test_first(self):
		#print("qwe",self.user.first_name,"ads",self.user.phone,self.user.designation,self.user.password)
		user=CustomUser.objects.get(id=19)
		self.assertEquals(int(user.count),4)

	def test_signup(self):
		client=Client()
		url=reverse('signup')
		response = client.get(url)
		self.assertEquals(response.status_code,200)

	def test_signup_data(self):
		client=Client()
		url=reverse('signup')
		req_data={
		"username": "mayur",
      	"first_name": "mayur",
      	"last_name": "prajapati",
      	"password":"password",
      	 "password1": "secret1"}

		
		response = self.client.post(url, req_data)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "users/signup.html")
		

	def test_signup_invaliddata(self):
		url=reverse('signup')
		req_data={
		"username": "mayur",
      	"first_name": "mayur",
      	"last_name": "prajapati",
      	"password1":"swiggy123",
      	 }
		client=Client()
		response=client.post(url,req_data)
		#response1=client.get('/users/')

		#self.assertContains('"error": This field is required.' in response.content)
		print(response)
		self.assertContains(response, "mayur")


		#self.assertEquals(response1.context['username'], "mayur")

class UserFormTest(TestCase):

	fixtures=['users/fixtures/users.json']

	@classmethod
	def setUpClass(cls):
		super(UserFormTest, cls).setUpClass()
		#self.user= CustomUser.objects.create()
		#import code; code.interact(local=dict(globals(), **locals()))
		print(CustomUser.objects.all())

	def test_form(self):
		#print("qwe",self.user.first_name,"ads",self.user.phone,self.user.designation,self.user.password)
		valid_data = {
		"password": "pbkdf2_sha256$150000$rThudk7McqVL$mhFHxWSf3pMFKm8pmobEIkTi3pudh1XDTun5I174bI0=",
		"username": "mayur",
		"first_name": "mayur",
		"last_name": "prajapati",
		"email": "mayurgmail.com",
		"contact": "",
		"state": 1,
		"city": 1,
		"address": "sabarmati",
		"pincode": 123456,
		}
		form = CustomUserCreationForm1(data = valid_data)
		form.is_valid()
		#print(form.errors)
		self.assertTrue(form.errors)
		print('innsdds')




