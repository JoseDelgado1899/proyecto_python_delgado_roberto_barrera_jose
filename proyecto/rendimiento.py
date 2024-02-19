import json

def cargarDatos():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: El archivo data.json no existe. Asegúrate de tener datos previos.")
        return None

def guardarDatos(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def evaluarRendimiento(data):
    rutas = data.get("rutas", [])
    campers = data.get("campers", [])

    for camper in campers:
        if "rutas" in camper:
            for ruta in camper["rutas"]:
                rutaActual = next((r for r in rutas if r["nombre"] == ruta), None)
                if rutaActual:
                    if "notas" in camper and ruta in camper["notas"] and camper["notas"][ruta] < 60:
                        print(f"Atención: El camper {camper['nombre']} tiene un rendimiento bajo en la ruta {ruta}.")
                       