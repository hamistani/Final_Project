from django.test import TestCase
from dogbreed.dog_breed_preference.controller import get_all_breeds
from dogbreed.dog_breed_preference.models import Breed

#Tests that get_all_breeds returns the correct number of Breed objects from the database
class ControllerTest(TestCase):
    def test_get_all_breeds_returns_correct_count(self):
        Breed.objects.create(breed_name="Husky", links="url1", image_url="img1")
        Breed.objects.create(breed_name="Beagles", links="url2", image_url="img2")
        all_breeds = get_all_breeds()
        self.assertEqual(len(all_breeds), 2)
