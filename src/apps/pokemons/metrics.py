from prometheus_client import Counter


pokemon_register = Counter('pokemon_register', 'number of pokemon created')