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

def evaluarCamper(camper, pruebasTeoricas, pruebasPracticas, quizesTrabajos):
    pesoTeoria = 0.3
    pesoPractica = 0.6
    pesoQuizesTrabajos = 0.1

    nota_teoria = sum(pruebasTeoricas) / len(pruebasTeoricas)
    nota_practica = sum(pruebasPracticas) / len(pruebasPracticas)
    nota_quizes_trabajos = sum(quizesTrabajos) / len(quizesTrabajos)

    notaFinal = (nota_teoria * pesoTeoria) + (nota_practica * pesoPractica) + (nota_quizes_trabajos * pesoQuizesTrabajos)

    return notaFinal

def aprobarModulo(notaFinal):
    return notaFinal >= 60


data = cargarDatos()

if data:
    camper = data["campers"][0]
    
    
    pruebasTeoricas = [70, 80, 75]
    pruebasPracticas = [65, 75, 70]
    quizesTrabajos = [8, 9, 7]

    notaFinal = evaluarCamper(camper, pruebasTeoricas, pruebasPracticas, quizesTrabajos)
    if aprobarModulo(notaFinal):
        print(f"El camper {camper['nombre']} ha aprobado el módulo con una nota final de {notaFinal}.")
    else:
        print(f"El camper {camper['nombre']} ha reprobado el módulo con una nota final de {notaFinal}.")