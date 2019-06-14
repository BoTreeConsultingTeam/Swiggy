from django.test import TestCase

# Create your tests here.
from .models import State,City

class StateAndCityModelTest(TestCase):
	def setUp(self):
		self.state=State.objects.create(statename='Gujarat')
		self.city=City.objects.create(state=self.state,cityname="asd")

	def test_statename(self):
		self.assertEqual(self.state.statename,'Gujarat')

	def test_cityname(self):
		self.assertFalse(self.city.cityname=='qwe')
		self.assertTrue(self.city.cityname=='asd')



