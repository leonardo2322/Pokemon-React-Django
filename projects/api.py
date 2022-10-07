from urllib import response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser,FileUploadParser

from rest_framework.response import Response
import json
from .serializers import ProjectSerializer
from .models import PokemonsBBDD


class PokemonsViewSets(APIView):

    parser_classes = (MultiPartParser, FormParser, JSONParser,FileUploadParser)

    def get(self, request,pk=0,format= None, *args, **kwargs):
        if (pk>0):
            pokemon = list(PokemonsBBDD.objects.filter(id=pk).values())
            if len(pokemon)>0:
                pokemons = pokemon[0]
                datos ={'message':"Succes","pokemones": pokemons}
            else:
                datos = {"message":"list pokemons not found"}
            return Response(datos,status=status.HTTP_200_OK)
        
        else:

            queryset = PokemonsBBDD.objects.all()
            # pokemonId = PokemonsBBDD.objects.get()
            serializer = ProjectSerializer(queryset, many=True)
            

            if len(queryset)>0:
                    datos = {'message':"Succes","pokemones":serializer.data}
            else:
                    datos = {"message":"list pokemons not found"}
            return Response(datos,status=status.HTTP_200_OK)
    
    
    def post(self, request, format= None):
        serialize = ProjectSerializer(data=request.data)
        if serialize.is_valid():
                serialize.save()
                return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

 
    def put(self,request,format= None,*args,**kwargs):
        if request.method == 'POST':
            print(request.data)
            serialeze = ProjectSerializer(request,data = request.data)
            if serialeze.is_valid():
                serialeze.save()
                return Response(serialeze.data,status=status.HTTP_200_OK)
        return Response(serialeze.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=0,format= None,*args,**kwargsl):
        
        pokemon = PokemonsBBDD.objects.filter(id = pk).first()
        if pokemon:
            pokemon.delete()
            return Response({'message':'dato ELiminado'},status=status.HTTP_200_OK)
        else:
            return Response({'messageToFailed':'no se encontro pokemon'},status=status.HTTP_400_BAD_REQUEST)