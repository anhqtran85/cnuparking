from django.test import TestCase, Client
from django.urls import reverse
from main.models import Parking_A

import json

# class TestViews(TestCase):


# 	def test_parkinga_page(self):
# 		client = Client()
# 		reponse = client.get(reverse('parkinga'))
# 		self.assertEquals(reponse.status_code, 200)
# 		self.assertTemplateUsed(reponse, 'parkinga.html')
# 		pass