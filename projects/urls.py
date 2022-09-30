from django.urls import path

from .api import PokemonsViewSets, pokemons_detail_view

urlpatterns= [
    path('api/', PokemonsViewSets.as_view(), name='api_pokemons'),
    path('api/<int:pk>/', pokemons_detail_view, name='pokemon_detail_api_view')
]