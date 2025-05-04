from django.test import TestCase
from dogbreed.dog_breed_preference.models import Breed

#Tests the Breed model’s string representation and field assignments for correctness
class BreedModelTest(TestCase):
    def test_str_method(self):
        breed = Breed.objects.create(
            breed_name="Beagles", links="https://example.com", image_url="https://image.jpg"
        )
        self.assertEqual(str(breed), "Beagles")

    def test_breed_fields(self):
        breed = Breed.objects.create(
            breed_name="Labrador", links="https://labrador.com", image_url="https://labrador.jpg"
        )
        self.assertEqual(breed.breed_name, "Labrador")
        self.assertEqual(breed.links, "https://labrador.com")
        self.assertEqual(breed.image_url, "https://labrador.jpg")
