import requests
import threading


class Pokemon(threading.Thread):
    def __init__(self, id):
        super().__init__()  # Llama al constructor de la clase base
        self.id = id  # Guarda el ID del Pokémon

    def run(self):
        data = get_pokemon(self.id)
        if data:
            # Extraemos el nombre del Pokémon
            name = data.get('name')

            # Extraemos las estadísticas (stats)
            stats = {stat['stat']['name']: stat['base_stat'] for stat in data.get('stats', [])}

            # Extraemos los tipos (types)
            types = [t['type']['name'] for t in data.get('types', [])]

            print(f"Nombre: {name}\nTipos: {types}\nEstadísticas: {stats}")


def get_pokemon(id):
    # Realizamos la solicitud a la API
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')  # ID dinámico
    if r.status_code == 200:
        return r.json()  # Convertimos la respuesta JSON en un diccionario
    else:
        print(f"Error al obtener el Pokémon {id}: Código de estado {r.status_code}")
        return None


# Crear y ejecutar hilos
pokemones = [Pokemon(i + 1) for i in range(50)]  # Crea 50 hilos para los primeros 50 Pokémon

for pokemon in pokemones:
    pokemon.start()  # Inicia cada hilo

for pokemon in pokemones:
    pokemon.join()  # Espera a que todos los hilos terminen
