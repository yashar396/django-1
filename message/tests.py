from django.test import SimpleTestCase
from django.urls import reverse

class MessagePageTests(SimpleTestCase):

    def test_url_exist_at_correct_location(self):
        response = self.client.get("//")
        self.assertEqual(response.status_code,200)

    def test_url_avalaible_by_name(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code,200)

