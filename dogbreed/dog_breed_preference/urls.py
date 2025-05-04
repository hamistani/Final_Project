from django.urls import path
from . import views

urlpatterns = [
    path('', views.breed_list, name='breed_list'),  
    path('traits/', views.breed_traits_view, name='breed_traits'), 
    path('user-preference/', views.user_preference_view, name='user_preference'), 
    path('rank/', views.breed_rank_view, name='breed_rank'),
    path('trait-description/', views.trait_description_view, name='trait_description'),
]