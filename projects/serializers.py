from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import PokemonsBBDD


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonsBBDD
        fields = ('id', 'nombre', 'categoria', 'habilidades', 'dano', 'img')