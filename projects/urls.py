from django.urls import path

from .api import PokemonsViewSets

urlpatterns= [
    path('api/', PokemonsViewSets.as_view(), name='api_pokemons'),
    path('api/<int:pk>/', PokemonsViewSets.as_view(), name='pokemon_process'),
    
]
