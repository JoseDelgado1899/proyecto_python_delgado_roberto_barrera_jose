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

def asignarARuta(camper, ruta, areaEntrenamiento):
    if "rutas" not in camper:
        camper["rutas"] = []

    if "areasEntrenamiento" not in camper:
        camper["areasEntrenamiento"] = []

    if areaEntrenamiento["cuposDisponibles"] > 0:
        camper["rutas"].append(ruta)
        camper["areasEntrenamiento"].append(areaEntrenamiento["nombre"])
        areaEntrenamiento["cuposDisponibles"] -= 1
        print(f"{camper['nombre']} asignado a la ruta {ruta} en el área de entrenamiento {areaEntrenamiento['nombre']}.")
        return True
    else:
        print(f"No hay cupos disponibles en el área de entrenamiento {areaEntrenamiento['nombre']} para {camper['nombre']}.")
        return False

def asignarCampersARutas(data):
    rutas = data.get("rutas", [])
    campers = data.get("campers", [])
    areasEntrenamiento = data.get("areasEntrenamiento", [])

    for camper in campers:
        if camper["estado"] == "Aprobado":
            for ruta in rutas:
                if ruta["nombre"] in camper["rutas"]:
                    for areaEntrenamiento in areasEntrenamiento:
                        if areaEntrenamiento["nombre"] == ruta["areaEntrenamiento"]:
                            asignarARuta(camper, ruta["nombre"], areaEntrenamiento)
                            break
data = cargarDatos()
if data:
    asignarCampersARutas(data)
    guardarDatos(data)