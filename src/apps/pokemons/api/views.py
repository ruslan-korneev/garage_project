from rest_framework.generics import CreateAPIView

from apps.pokemons import metrics
from apps.pokemons.models import Pokemon
from apps.pokemons.api.serializers import PokemonCreateSerializer


class PokemonCreateAPIView(CreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_classes = PokemonCreateSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        metrics.pokemon_created.inc()