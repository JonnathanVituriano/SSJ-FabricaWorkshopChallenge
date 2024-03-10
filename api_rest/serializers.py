from rest_framework import serializers
from .models import Pokemons

class PokemonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pokemons
        fields = ('id', 'name', 'height', 'weight', 'tipo_pokemon')
