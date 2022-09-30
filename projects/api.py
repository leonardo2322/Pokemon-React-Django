from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from rest_framework.response import Response

from .serializers import ProjectSerializer
from .models import PokemonsBBDD


class PokemonsViewSets(APIView):

    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, *args, **kwargs):
        queryset = list(PokemonsBBDD.objects.all())
        serializer = ProjectSerializer(queryset, many=True)
        
        if len(queryset)>0:
            datos = {'message':"Succes","pokemones":serializer.data}
        else:
            datos = {"message":"list pokemons not found"}
        return Response(datos,status=status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):
        serialize = ProjectSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def pokemons_detail_view(request,pk):
    pokemon = PokemonsBBDD.objects.filter(id = pk).first()
    if pokemon:  
        if request.method == 'PUT':
            serialeze = ProjectSerializer(pokemon,data = request.data)
            if pokemon.is_valid():
                serialeze.save()
                return Response(serialeze.data,status=status.HTTP_200_OK)
            return Response(serialeze.errors,status=status.HTTP_400_BAD_REQUEST)

        elif  request.method == 'DELETE':
            pokemon.delete()
            return Response({'message':'dato ELiminado'},status=status.HTTP_200_OK)

    return Response({'messageToFailed':'no se encontro pokemon'},status=status.HTTP_400_BAD_REQUEST)