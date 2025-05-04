from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command
from dogbreed.dog_breed_preference.models import Breed, UserPreference

class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.breed = Breed.objects.create(
            breed_name="Husky", links="https://husky.com", image_url="https://husky.jpg"
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse('breed_list'))
        self.assertEqual(response.status_code, 200)

    def test_trait_page_loads(self):
        response = self.client.get(reverse('breed_traits'))
        self.assertEqual(response.status_code, 200)

    def test_preference_page_loads(self):
        response = self.client.get(reverse('user_preference'))
        self.assertEqual(response.status_code, 200)

    def test_breed_match_logic(self):
        response = self.client.get(reverse('breed_list'))
        self.assertContains(response, self.breed.breed_name)

    def test_load_data_execution(self):
        call_command('load_data')
        self.assertGreaterEqual(Breed.objects.count(), 1)
