
from django.shortcuts import render
from django.http.response import JsonResponse
# from django.views import View
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from .models import PokemonsBBDD
from .serializers import ProjectSerializer
# Create your views here.
# AQUI DEBO OBTENER LOS CAMPOS DE REACT JSON RESPONSE

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = PokemonsBBDD.objects.all()
    serializer_class = ProjectSerializer(queryset, many=True)
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.AllowAny]


class PokemonsView(viewsets.ModelViewSet):
    
    def get(self, request, *args, **kwargs):
        pokemones = list(PokemonsBBDD.objects.values())
        serializer_class = ProjectSerializer(pokemones, many=True)
        if len(pokemones)>0:
           
            datos = {'message':"Succes","pokemones":pokemones}
        else:
            datos = {"message":"list pokemons not found"}
        return JsonResponse(datos)
    @action(detail=True, methods=['post', 'delete'])
    def post():
            pass
  
    def put():
        pass
    def delete():
        pass
    @classmethod
    def get_extra_actions(cls):
        return []
