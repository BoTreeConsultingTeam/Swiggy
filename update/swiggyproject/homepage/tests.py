from django.test import TestCase,Client
from django.urls import reverse

# Create your tests here.
class HomePageTest(TestCase):
	fixtures=['users/fixtures/alldata.json']

	@classmethod
	def setUpClass(cls):
		super(HomePageTest, cls).setUpClass()
		
	def test_Test(self):
		client=Client()
		response=client.get(reverse('index'))
		self.assertEquals(response.status_code,200)

	def test_FoodTest(self):
		client=Client()
		response=client.get(reverse('food'),{'id':15})
		self.assertEquals(response.status_code,200)

	def test_searchResults(self):
		client=Client()
		response=client.get(reverse('search'),{'searchinput':'Honest'})
		self.assertEquals(response.status_code,200)		

