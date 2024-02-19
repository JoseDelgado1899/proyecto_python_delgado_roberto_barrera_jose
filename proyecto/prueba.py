import json

def cargar_datos():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: El archivo data.json no existe. Asegúrate de tener datos previos.")
        return None

def guardar_datos(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def registrar_notas(coordinador, campers):
    if coordinador["rol"] == "coordinador":
        print("Lista de campers:")
        for i, camper in enumerate(campers, start=1):
            print(f"{i}. {camper['nombre']} - Estado: {camper['estado']}")
        
        try:
            indice_camper = int(input("Seleccione el número del camper al que desea registrar notas: ")) - 1
            selected_camper = campers[indice_camper]

            nota_teorica = float(input("Ingrese la nota teórica: "))
            nota_practica = float(input("Ingrese la nota práctica: "))

            promedio = (nota_teorica + nota_practica) / 2

            if promedio >= 60:
                selected_camper["estado"] = "Aprobado"
                print(f"Notas registradas para {selected_camper['nombre']}. Estado actual: {selected_camper['estado']}")
            else:
                print(f"El camper {selected_camper['nombre']} no alcanzó el promedio mínimo de 60.")
            if promedio <= 60:
                selected_camper["estado"] = "no aprobado"
                print(f"Notas registradas para {selected_camper['nombre']}. Estado actual: {selected_camper['estado']}")

            return campers

        except (ValueError, IndexError):
            print("Error: Selección inválida.")
    
    else:
        print("Error: El usuario no tiene permisos para registrar notas.")
    
    return campers

def menu_principal():
    data = cargar_datos()
    if data is None:
        return

    campers = data.get("campers", [])
    coordinador = {"rol": "coordinador", "nombre": "Coordinador1"} 
    
    while True:
        print("1. Ver lista de campers")
        print("2. Registrar notas (Solo Coordinador)")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Lista de campers:")
            for i, camper in enumerate(campers, start=1):
                print(f"{i}. {camper['nombre']} - Estado: {camper['estado']}")

        elif opcion == "2":
            campers = registrar_notas(coordinador, campers)
            guardar_datos(data)

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_principal()