from .models import PokemonsBBDD

from rest_framework import viewsets, permissions

from .serializers import ProjectSerializer


class PokemonsViewSets(viewsets.ModelViewSet):
    queryset = PokemonsBBDD.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer