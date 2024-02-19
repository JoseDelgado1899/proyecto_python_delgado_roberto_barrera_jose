import json

def cargarDatos():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: El archivo data.json no existe. Asegúrate de tener datos previos.")
        return None

def listarCampersInscritos(data):
    campers = data.get("campers", [])
    campersInscritos = [camper for camper in campers if camper["estado"] == "Inscrito"]
    return campersInscritos

def listarCampersAprobadosExamenInicial(data):
    campers = data.get("campers", [])
    campersAprobados = [camper for camper in campers if camper["estado"] == "Aprobado"]
    return campersAprobados

def listarEntrenadoresTrabajando(data):
    trainers = data.get("trainers", [])
    return trainers

def listarCampersBajoRendimiento(data):
    campers = data.get("campers", [])
    campersBajoRendimiento = [camper for camper in campers if camper.get("rendimiento") == "Bajo"]
    return campersBajoRendimiento

def listarCampersYTrainersPorRuta(data, ruta):
    ruta = data.get("rutas", [])
    campers = data.get("campers", [])
    trainers = data.get("trainers", [])

    campersRuta = [camper for camper in campers if "rutas" in camper and ruta in camper["rutas"]]
    trainersRuta = [trainer for trainer in trainers if "rutas" in trainer and ruta in trainer["rutas"]]

    return campersRuta, trainersRuta

def mostrarCampersAprobadosYPerdidosPorModulo(data, ruta, trainer):
    rutas = data.get("rutas", [])
    campers = data.get("campers", [])
    trainers = data.get("trainers", [])

    if ruta not in [r["nombre"] for r in rutas]:
        print("Error: La ruta especificada no existe.")
        return

    if trainer not in [t["nombre"] for t in trainers]:
        print("Error: El entrenador especificado no existe.")
        return

    campersRutaTrainer = [camper for camper in campers if "rutas" in camper and "trainers" in camper
                            and ruta in camper["rutas"] and trainer in camper["trainers"]]

    aprobadosPorModulo = {f"Módulo {i + 1}": 0 for i in range(len(rutas[ruta]["modulos"]))}
    perdidosPorModulo = {f"Módulo {i + 1}": 0 for i in range(len(rutas[ruta]["modulos"]))}

    for camper in campersRutaTrainer:
        if "notas" in camper:
            for i, nota in enumerate(camper["notas"][ruta]):
                if nota >= 60:
                    aprobadosPorModulo[f"Módulo {i + 1}"] += 1
                else:
                    perdidosPorModulo[f"Módulo {i + 1}"] += 1

    print(f"Campers aprobados y perdidos por módulo en la ruta {ruta} con el entrenador {trainer}:")
    print("Aprobados:")
    for modulo, cantidad in aprobadosPorModulo.items():
        print(f"{modulo}: {cantidad} campers")
    print("Perdidos:")
    for modulo, cantidad in perdidosPorModulo.items():
        print(f"{modulo}: {cantidad} campers")


data = cargarDatos()

if data:
    campersInscritos = listarCampersInscritos(data)
    print("Campers en estado de inscrito:")
    for camper in campersInscritos:
        print(camper)

    campersAprobadosExamenInicial = listarCampersAprobadosExamenInicial(data)
    print("\nCampers que aprobaron el examen inicial:")
    for camper in campersAprobadosExamenInicial:
        print(camper)

    trainersTrabajando = listarEntrenadoresTrabajando(data)
    print("\nEntrenadores trabajando con CampusLands:")
    for trainer in trainersTrabajando:
        print(trainer)

    campersBajoRendimiento = listarCampersBajoRendimiento(data)
    print("\nCampers con bajo rendimiento:")
    for camper in campersBajoRendimiento:
        print(camper)

    rutaEspecifica = ""  
    campersRuta, trainersRuta = listarCampersYTrainersPorRuta(data, rutaEspecifica)
    print(f"\nCampers asociados a la ruta {rutaEspecifica}:")
    