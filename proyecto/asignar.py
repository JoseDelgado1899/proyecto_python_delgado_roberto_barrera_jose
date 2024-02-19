import json

def asignarCampersARutas(data):
    rutas = data.get("rutas", [])
    campers = data.get("campers", [])
    areasEntrenamiento = data.get("AreasEntrenamiento", [])

    for camper in campers:
        if camper["estado"] == "Aprobado" and not camper.get("rutas"):
            for ruta in rutas:
                for areaEntrenamiento in areasEntrenamiento:
                    if (
                        ruta["nombre"] == areaEntrenamiento["ruta"] and
                        areaEntrenamiento["cuposdisponibles"] > 0
                    ):
                        asignarARuta(camper, ruta["nombre"], areaEntrenamiento)
                        break

def asignarARuta(camper, ruta, areaEntrenamiento):
    if "rutas" not in camper:
        camper["rutas"] = []

    if "areasEntrenamiento" not in camper:
        camper["areasEntrenamiento"] = []

    camper["rutas"].append(ruta)
    camper["areasEntrenamiento"].append(areaEntrenamiento["nombre"])
    areaEntrenamiento["cupos_disponibles"] -= 1
    print(f"{camper['nombre']} asignado a la ruta {ruta} en el área de entrenamiento {areaEntrenamiento['nombre']}.")