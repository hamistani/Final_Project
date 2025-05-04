from .models import Breed, BreedTrait, BreedRank, UserPreference, TraitDescription

def get_all_breeds():
    """Fetch all breeds."""
    return Breed.objects.all()

def get_all_traits():
    """Fetch all breed traits."""
    return BreedTrait.objects.all()

def get_all_ranks():
    """Fetch all breed ranks."""
    return BreedRank.objects.all()

def get_all_user_preferences():
    """Fetch all user preferences."""
    return UserPreference.objects.all()

def get_all_breed_ranks():
    """Fetch all breed rankings."""
    return BreedRank.objects.all()

def get_all_trait_descriptions():
    """Fetch all trait descriptions."""
    return TraitDescription.objects.all()
