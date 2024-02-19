import json

data = {
    "rutas": [
        {"nombre": "Ruta NodeJS", "AreaEntrenamiento": "sputnik"},
        {"nombre": "Ruta Java", "AreaEntrenamiento": "Artemis"},
        {"nombre": "Ruta NetCore", "AreaEntrenamiento": "Apolo"}
    ],
    "campers": [
        {"nombre": "Camper1", "estado": "Aprobado", "rutas": []},
        {"nombre": "Camper2", "estado": "Aprobado", "rutas": []}
    ],
    "AreasEntrenamiento": [
        {"nombre": "sputnik", "cuposDisponibles": 33},
        {"nombre": "Artemis", "cuposDisponibles": 33},
        {"nombre": "Apolo", "cuposDisponibles": 33}
    ]
}

with open('rutas.json', 'w') as file:
    json.dump(data, file, indent=4)
