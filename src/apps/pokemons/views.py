from django.http.response import HttpResponse
from apps.pokemons.models import Pokemon



def metrics_view(request):
    data = '''
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 12594.0
python_gc_objects_collected_total{generation="1"} 1567.0
python_gc_objects_collected_total{generation="2"} 101.0
'''
    # data = """
    # # HELP django_pokemon_objects_collected_total Objects collected during django
    # # TYPE django_pokemon_objects_collected_total counter
    # """
    data += f"django_pokemon_objects_number_of_pokemon {Pokemon.objects.all().count()}\n"
    data += f"django_pokemon_objects_number_of_pikachu {Pokemon.objects.filter(name='Pikachu').count()}\n"
    return HttpResponse(data)


