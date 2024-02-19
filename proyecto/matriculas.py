def matricularCamper(data, camper, ruta, trainer, fechaInicio, fechaFinalizacion, salonEntrenamiento):
    campers = data.get("campers", [])
    trainers = data.get("Trainers", [])
    rutas = data.get("rutas", [])
    if camper["estado"] == "Aprobado":
        if ruta in [r["nombre"] for r in rutas]:
            if trainer in [t["nombre"] for t in trainers]:
                assigned_rutas = trainers[[t["nombre"] == trainer for t in trainers.index]["rutas"]]
                if ruta in assigned_rutas:
                    campers[[c["nombre"] == camper["nombre"] for c in campers.index]["rutas"].append(ruta)]
                    matricula = {
                        "camper": camper["nombre"],
                        "ruta": ruta,
                        "trainer": trainer,
                        "fechaInicio": fechaInicio.strftime("%Y-%m-%d"),
                        "fechaFinalizacion": fechaFinalizacion.strftime("%Y-%m-%d"),
                        "salonEntrenamiento": salonEntrenamiento
                    }
                    if "matriculas" not in data:
                        data["matriculas"] = []

                    data["matriculas"].append(matricula)
                    print(f"{camper['nombre']} matriculado en la ruta {ruta} con el trainer {trainer}.")
                    return

    print(f"Error: No se puede matricular a {camper['nombre']} en la ruta {ruta}.")