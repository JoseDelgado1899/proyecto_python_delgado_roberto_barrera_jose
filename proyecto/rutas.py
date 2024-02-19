def crearRutaEntrenamiento(nombreRuta, modulos):
    nuevaRuta = {
        "nombre": nombreRuta,
        "modulos": modulos
    }
    return nuevaRuta

rutaNodejs = crearRutaEntrenamiento("Ruta NodeJS", ["Fundamentos de programación", "Programación Web", "Backend"])
rutaJava = crearRutaEntrenamiento("Ruta Java", ["Fundamentos de programación", "Programación formal", "Backend"])
rutaNetcore = crearRutaEntrenamiento("Ruta NetCore", ["Fundamentos de programación", "Programación formal", "Backend"])


def crearNuevaRuta():
    NuevaRuta = {}

    NuevaRuta["nombre"] = input("Ingrese el nombre de la nueva ruta de entrenamiento: ")
    NuevaRuta["modulos"] = [
        "Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)",
        "Programación Web (HTML, CSS y Bootstrap)",
        "Programación formal (Java, JavaScript, C#)",
        "Bases de datos (Mysql, MongoDb y Postgresql)",
        "Backend (NetCore, Spring Boot, NodeJS y Express)"
    ]

    
    print("Ingrese la información para las Bases de datos:")
    NuevaRuta["sgdb principal"] = input("SGDB principal: ")
    NuevaRuta["sgdb alternativo"] = input("SGDB alternativo: ")

    return NuevaRuta

def agregarNuevaRuta(data):
    if "rutas" not in data:
        data["rutas"] = []

    nuevaRuta = crearNuevaRuta()
    data["rutas"].append(nuevaRuta)
    print(f"La ruta {nuevaRuta['nombre']} ha sido creada y agregada correctamente.")
crearNuevaRuta()
agregarNuevaRuta()