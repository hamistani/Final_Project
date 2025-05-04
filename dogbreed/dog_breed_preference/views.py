from django.shortcuts import render
from .controller import get_all_breeds, get_all_traits, get_all_user_preferences, get_all_breed_ranks, get_all_trait_descriptions

def breed_list(request):
    """View for listing all breeds."""
    breeds = get_all_breeds() 
    return render(request, 'breed_list.html', {'breeds': breeds})

def breed_traits_view(request):
    """View for listing all breed traits."""
    traits = get_all_traits()  
    return render(request, 'breed_traits.html', {'traits': traits})

def user_preference_view(request):
    """View for listing all user preferences."""
    preferences = get_all_user_preferences()
    return render(request, 'user_preference.html', {'preferences': preferences})

def breed_rank_view(request):
    """View for listing all breed rankings."""
    ranks = get_all_breed_ranks()
    return render(request, 'breed_rank.html', {'ranks': ranks})

def trait_description_view(request):
    """View for listing all trait descriptions."""
    descriptions = get_all_trait_descriptions()
    return render(request, 'trait_description.html', {'descriptions': descriptions})