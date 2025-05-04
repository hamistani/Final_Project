from django.db import models
from django.conf import settings

class Breed(models.Model):
    breed_id = models.AutoField(primary_key=True)
    breed_name = models.CharField(max_length=100, unique=True)
    links = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.breed_name
    
class BreedRank(models.Model):
    breed_name = models.OneToOneField(Breed, on_delete=models.CASCADE, related_name="rank")
    rank_2013 = models.PositiveIntegerField()
    rank_2014 = models.PositiveIntegerField()
    rank_2015 = models.PositiveIntegerField()
    rank_2016 = models.PositiveIntegerField()
    rank_2017 = models.PositiveIntegerField()
    rank_2018 = models.PositiveIntegerField()
    rank_2019 = models.PositiveIntegerField()
    rank_2020 = models.PositiveIntegerField()

    def __str__(self):
        return f"Rankings for {self.breed}"

class BreedTrait(models.Model):
    breed_name = models.OneToOneField(Breed, on_delete=models.CASCADE, db_column='breed_name', related_name="traits")  
    affectionate_with_family = models.PositiveIntegerField()
    good_with_young_children = models.PositiveIntegerField()
    good_with_other_dogs = models.PositiveIntegerField()
    shedding_level = models.PositiveIntegerField()
    coat_grooming_frequency = models.PositiveIntegerField()
    drooling_level = models.PositiveIntegerField()
    coat_type = models.CharField(max_length=50)
    coat_length = models.CharField(max_length=50)
    openness_to_strangers = models.PositiveIntegerField()
    playfullness_level = models.PositiveIntegerField()
    watchdog_protective_nature = models.PositiveIntegerField()
    adaptability_level = models.PositiveIntegerField()
    trainability_level = models.PositiveIntegerField()
    energy_level = models.PositiveIntegerField()
    barking_level = models.PositiveIntegerField()
    mental_stimulation = models.PositiveIntegerField()

    def __str__(self):
        return f"Traits for {self.breed_name.breed_name}"
    
class TraitDescription(models.Model):
    trait_id = models.AutoField(primary_key=True)  
    trait = models.CharField(max_length=100, unique=True)  
    trait_1 = models.CharField(max_length=100)
    trait_5 = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.trait
    
class UserPreference(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)  # Unique Key
    breed_id = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, db_column='breed_id', related_name="user_preferences")  
    affectionate_with_family = models.PositiveIntegerField()
    good_with_young_children = models.PositiveIntegerField()
    good_with_other_dogs = models.PositiveIntegerField()
    shedding_level = models.PositiveIntegerField()
    coat_grooming_frequency = models.PositiveIntegerField()
    drooling_level = models.PositiveIntegerField()
    coat_type = models.CharField(max_length=50)
    coat_length = models.CharField(max_length=50)
    openness_to_strangers = models.PositiveIntegerField()
    playfullness_level = models.PositiveIntegerField()
    watchdog_protective_nature = models.PositiveIntegerField()
    adaptability_level = models.PositiveIntegerField()
    trainability_level = models.PositiveIntegerField()
    energy_level = models.PositiveIntegerField()
    barking_level = models.PositiveIntegerField()
    mental_stimulation = models.PositiveIntegerField()

    def __str__(self):
        return f"Preferences of {self.username}"