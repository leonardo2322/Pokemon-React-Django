from rest_framework import serializers
from .models import PokemonsBBDD


class ProjectSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True,required=False)
    class Meta(object):
        model = PokemonsBBDD
        fields = ('id', 'nombre', 'categoria', 'habilidades', 'dano', 'img')
        
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'categoria':instance.categoria,
            'habilidades':instance.habilidades,
            'dano':instance.dano,
            'img':instance.img.url
            
        }