from django.core.management import call_command
from django.test import TestCase
from dogbreed.dog_breed_preference.models import Breed
import os

class LoadDataTest(TestCase):
    def test_command_runs(self):
        call_command('load_data')
        self.assertGreaterEqual(Breed.objects.count(), 1, "No breeds were loaded by load_data command.")