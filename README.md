# Pokemones paralelos

## Alumnos 
 - Felipe Martinez Reyna
 - Gerardo Issac Luna Rodarte
 - Cristopher Isaí Velázquez Medina
 - Rodrigo Emiliano Maldonado de la Cruz
 -  Rogelio Bustamante Ibarra
 

## Pokemon Multi-threaded Fetcher

Este programa utiliza múltiples hilos para recuperar información de los primeros 50 Pokémon desde la API de PokeAPI. Escrito en Python, combina el uso de la biblioteca requests para realizar solicitudes HTTP y threading para ejecutar múltiples tareas simultáneamente

### Características
- Recupera información básica sobre los Pokémon: nombre, tipos, y estadísticas base.
- Utiliza hilos para acelerar la recuperación de datos, ejecutando 50 solicitudes concurrentemente.
- Muestra la información obtenida en la consola.
### Requisitos

- Python 3.6 o superior

- Biblioteca requests instalada:
## Estructura del Código

## Explicacion del codigo
#### Clases y Funciones

**Pokemon (Clase)**:
Una subclase de threading.Thread. Cada instancia representa un hilo que solicita información de un Pokémon específico usando su ID.

- Métodos principales:
  - __init__(id): Inicializa el hilo con el ID del Pokémon.
  - run(): Realiza la solicitud y extrae los datos relevantes     (nombre, tipos, estadísticas) para mostrarlos en la consola.

- get_pokemon(id) (Función)
Realiza una solicitud HTTP a la API de PokeAPI con el ID del Pokémon.
Si la solicitud es exitosa, devuelve un diccionario con los datos del Pokémon; de lo contrario, muestra un mensaje de error.

- Ejecución del Programa
  - Crear hilos:
    Se crea una lista de 50 instancias de la clase Pokemon, cada una asignada a un ID único (del 1 al 50).

- Iniciar hilos:
  - Los hilos se inician en paralelo con start().

- Sincronización:
    - Se espera a que todos los hilos terminen su ejecución usando join().

### Ejemplo de salida

Nombre: bulbasaur
Tipos: ['grass', 'poison']
Estadísticas: {'hp': 45, 'attack': 49, 'defense': 49, 'special-attack': 65, 'special-defense': 65, 'speed': 45}

Nombre: charmander
Tipos: ['fire']
Estadísticas: {'hp': 39, 'attack': 52, 'defense': 43, 'special-attack': 60, 'special-defense': 50, 'speed': 65}
...



# Pokemones paralelos

## Alumnos 
 - Felipe Martinez Reyna
 - Gerardo Issac Luna Rodarte
 - Cristopher Isaí Velázquez Medina
 - Rodrigo Emiliano Maldonado de la Cruz
 -  Rogelio Bustamante Ibarra
 

## Pokemon Multi-threaded Fetcher

Este programa utiliza múltiples hilos para recuperar información de los primeros 50 Pokémon desde la API de PokeAPI. Escrito en Python, combina el uso de la biblioteca requests para realizar solicitudes HTTP y threading para ejecutar múltiples tareas simultáneamente

### Características
- Recupera información básica sobre los Pokémon: nombre, tipos, y estadísticas base.
- Utiliza hilos para acelerar la recuperación de datos, ejecutando 50 solicitudes concurrentemente.
- Muestra la información obtenida en la consola.
### Requisitos

- Python 3.6 o superior

- Biblioteca requests instalada:

## Explicacion del codigo
#### Clases y Funciones

**Pokemon (Clase)**:
Una subclase de threading.Thread. Cada instancia representa un hilo que solicita información de un Pokémon específico usando su ID.

- Métodos principales:
  - __init__(id): Inicializa el hilo con el ID del Pokémon.
  - run(): Realiza la solicitud y extrae los datos relevantes     (nombre, tipos, estadísticas) para mostrarlos en la consola.

- get_pokemon(id) (Función)
Realiza una solicitud HTTP a la API de PokeAPI con el ID del Pokémon.
Si la solicitud es exitosa, devuelve un diccionario con los datos del Pokémon; de lo contrario, muestra un mensaje de error.

- Ejecución del Programa
  - Crear hilos:
    Se crea una lista de 50 instancias de la clase Pokemon, cada una asignada a un ID único (del 1 al 50).

- Iniciar hilos:
  - Los hilos se inician en paralelo con start().

- Sincronización:
    - Se espera a que todos los hilos terminen su ejecución usando join().

### Ejemplo de salida
```bash
Nombre: bulbasaur
Tipos: ['grass', 'poison']
Estadísticas: {'hp': 45, 'attack': 49, 'defense': 49, 'special-attack': 65, 'special-defense': 65, 'speed': 45}

Nombre: charmander
Tipos: ['fire']
Estadísticas: {'hp': 39, 'attack': 52, 'defense': 43, 'special-attack': 60, 'special-defense': 50, 'speed': 65}
...
```

## Consideraciones

- Limitaciones de la API:
    PokeAPI puede tener límites en el número de solicitudes por segundo. Ajusta el número de hilos si experimentas problemas de tasa de límite.

- Manejo de errores:
    Si un hilo no puede obtener datos debido a un problema de red o un ID inválido, se mostrará un mensaje de error con el código de estado HTTP.




