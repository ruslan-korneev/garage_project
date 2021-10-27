from rest_framework import serializers
from apps.pokemons.models import Pokeball, Pokemon


class PokeballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokeball
        fields = ('id', 'name', 'level')


class PokemonCreateSerializer(serializers.ModelSerializer):

    pokeball = PokeballSerializer

    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'level', 'pokeball')
