import os
import csv
from django.core.management.base import BaseCommand
from django.db import connection
from dogbreed.dog_breed_preference.models import Breed, BreedTrait, BreedRank, TraitDescription, UserPreference
import sys
print("Python Path:", sys.path)

class Command(BaseCommand):
    help = "Load data from CSV files into the database"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Breed.objects.all().delete()
        BreedTrait.objects.all().delete()
        BreedRank.objects.all().delete()
        TraitDescription.objects.all().delete()
        UserPreference.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('All existing data cleared!'))

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE dog_breed_preference_breedtrait_id_seq RESTART WITH 1;")

        self.stdout.write(self.style.SUCCESS('All existing data cleared and sequence reset!'))


        # Load Breed data
        with open('csv_files/breed.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Processing row in breed.csv: {row}")
                Breed.objects.get_or_create(
                    breed_id=row['breed_id'],
                    defaults={
                        'breed_name': row['breed_name'],
                        'links': row['links'],
                        'image_url': row['image_url'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Breed data loaded successfully!'))

        # Load BreedTrait data
        with open('csv_files/breed_traits.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            print(f"CSV headers: {reader.fieldnames}")
            for row in reader:
                print(f"Processing row in breed_traits.csv: {row}")
                breed_name = row.get('breed_name', '').strip()
                if not breed_name:
                    print("Error: Missing 'breed_name' in breed_traits. Skipping entry.")
                    continue
                try:
                    breed = Breed.objects.get(breed_name__iexact=breed_name)
                    BreedTrait.objects.get_or_create(
                        breed_name=breed,
                        defaults={
                            'affectionate_with_family': row['affectionate_with_family'],
                            'good_with_young_children': row['good_with_young_children'],
                            'good_with_other_dogs': row['good_with_other_dogs'],
                            'shedding_level': row['shedding_level'],
                            'coat_grooming_frequency': row['coat_grooming_frequency'],
                            'drooling_level': row['drooling_level'],
                            'coat_type': row['coat_type'],
                            'coat_length': row['coat_length'],
                            'openness_to_strangers': row['openness_to_strangers'],
                            'playfullness_level': row['playfullness_level'],
                            'watchdog_protective_nature': row['watchdog_protective_nature'],
                            'adaptability_level': row['adaptability_level'],
                            'trainability_level': row['trainability_level'],
                            'energy_level': row['energy_level'],
                            'barking_level': row['barking_level'],
                            'mental_stimulation': row['mental_stimulation'],
                        }
                    )
                except Breed.DoesNotExist:
                    print(f"Unmatched breed_name in breed_traits: '{breed_name}' - Skipping entry.")
                    continue
        self.stdout.write(self.style.SUCCESS('Breed traits loaded successfully!'))

        # Load BreedRank data
        # Load BreedRank data
        with open('csv_files/breed_rank.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Processing row in breed_rank.csv: {row}")
                breed_id = row.get('breed_id', '').strip()
                if not breed_id:
                    print("Error: Missing 'breed_id' in breed_rank. Skipping entry.")
                    continue
                try:
                    breed = Breed.objects.get(breed_id=breed_id)  # Lookup using breed_id
                    BreedRank.objects.get_or_create(
                        breed_name=breed,
                        defaults={
                            'rank_2013': row['rank_2013'],
                            'rank_2014': row['rank_2014'],
                            'rank_2015': row['rank_2015'],
                            'rank_2016': row['rank_2016'],
                            'rank_2017': row['rank_2017'],
                            'rank_2018': row['rank_2018'],
                            'rank_2019': row['rank_2019'],
                            'rank_2020': row['rank_2020'],
                        }
                    )
                except Breed.DoesNotExist:
                    print(f"Unmatched breed_id in breed_rank: '{breed_id}' - Skipping entry.")
                    continue
        self.stdout.write(self.style.SUCCESS('Breed rank data loaded successfully!'))

        # Load TraitDescription data
        with open('csv_files/trait_description.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Processing row in trait_description.csv: {row}")
                TraitDescription.objects.get_or_create(
                    trait_id=row['trait_id'],
                    defaults={
                        'trait': row['trait'],
                        'trait_1': row['trait_1'],
                        'trait_5': row['trait_5'],
                        'description': row['description'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Trait descriptions loaded successfully!'))

        # Load UserPreference data
        with open('csv_files/user_preference.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Processing row in user_preference.csv: {row}")
                breed_id = row.get('breed_id', '').strip()
                if not breed_id:
                    print("Error: Missing 'breed_id' in user_preference. Skipping entry.")
                    continue
                try:
                    breed = Breed.objects.get(breed_id=breed_id)
                    UserPreference.objects.get_or_create(
                        username=row['username'],
                        defaults={
                            'first_name': row['first_name'],
                            'last_name': row['last_name'],
                            'breed_id': breed,
                            'affectionate_with_family': row['affectionate_with_family'],
                            'good_with_young_children': row['good_with_young_children'],
                            'good_with_other_dogs': row['good_with_other_dogs'],
                            'shedding_level': row['shedding_level'],
                            'coat_grooming_frequency': row['coat_grooming_frequency'],
                            'drooling_level': row['drooling_level'],
                            'coat_type': row['coat_type'],
                            'coat_length': row['coat_length'],
                            'openness_to_strangers': row['openness_to_strangers'],
                            'playfullness_level': row['playfullness_level'],
                            'watchdog_protective_nature': row['watchdog_protective_nature'],
                            'adaptability_level': row['adaptability_level'],
                            'trainability_level': row['trainability_level'],
                            'energy_level': row['energy_level'],
                            'barking_level': row['barking_level'],
                            'mental_stimulation': row['mental_stimulation'],
                        }
                    )
                except Breed.DoesNotExist:
                    print(f"Unmatched breed_id in user_preference: '{breed_id}' - Skipping entry.")
                    continue
        self.stdout.write(self.style.SUCCESS('User preferences loaded successfully!'))