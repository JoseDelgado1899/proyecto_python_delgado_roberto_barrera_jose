
def asignarRutaATrainer(trainer, ruta, areaEntrenamiento):
    if "rutas" not in trainer:
        trainer["rutas"] = []

    if "areasEntrenamiento" not in trainer:
        trainer["areasEntrenamiento"] = []

    trainer["rutas"].append(ruta)
    trainer["areasEntrenamiento"].append(areaEntrenamiento["nombre"])
    print(f"{trainer['nombre']} asignado a la ruta {ruta} en el área de entrenamiento {areaEntrenamiento['nombre']}.")

def asignarTrainersARutas(data):
    rutas = data.get("rutas", [])
    trainers = data.get("Trainers", [])
    areasEntrenamiento = data.get("AreasEntrenamiento", [])

    for trainer in trainers:
        for ruta in rutas:
            for areaEntrenamiento in areasEntrenamiento:
                if (
                    ruta["nombre"] == areaEntrenamiento["ruta"] and
                    areaEntrenamiento["cupos_disponibles"] > 0 and
                    all(dia in trainer["horario"] for dia in areaEntrenamiento["horario"])
                ):
                    asignarRutaATrainer(trainer, ruta["nombre"], areaEntrenamiento)
                    areaEntrenamiento["cupos_disponibles"] -= 1
                    break