from django.contrib import admin
from .models import Pokemon, Pokeball


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'master', 'level', 'pokeball')
    list_filter = ('master', 'level')

@admin.register(Pokeball)
class PokeballAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
