from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import PokemonsBBDD
# Create your views here.
# AQUI DEBO OBTENER LOS CAMPOS DE REACT JSON RESPONSE

class PokemonsView(View):
    def get():
        pokemones = list(PokemonsBBDD.objects.values())
        if len(pokemones)>0:
            datos = {'message':"Succes","pokemones":pokemones}
        else:
            datos = {"message":"list pokemons not found"}
        return JsonResponse(datos)
    def post():
        pass
    def put():
        pass
    def delete():
        pass
    @classmethod
    def get_extra_actions(cls):
        return []
