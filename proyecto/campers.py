import json

def gestionCampers():
   
    campers = []
    while True:
        print("--------------------------------------------------------")
        print("")
        print("                   Menú Campers")
        print("")
        print("--------------------------------------------------------")
        print("1. Ver lista de campers")
        print("2. Agregar nuevo camper")
        print("3. Modificar información de un camper")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            with open("data.json") as file:
                data=json.load(file)
            for camper in data["campers"]:
                print("")
                print("nombre", camper["nombre"])
                print("apellido", camper["apellido"])
                print("direccion",camper["direccion"])
                print("acudiente",camper["acudiente"])
                print("telefono",camper["telefono"])
                print("estado",camper["estado"])
                print("riesgo",camper["riesgo"])
                print("")
          
        elif opcion == "2":
                with open("data.json","r") as file:
                    data=json.load(file)
            
                nuevoNombre = input("Ingrese el nombre del nuevo camper: ")
                nuevoApellido=input("ingrese apellido del camper: ")
                nuevaDireccion=input("ingrese direccion del camper: ")
                nuevoAcudiente=input("ingrese acudiente del camper: ")
                nuevoTelefono=input("ingrese telefono del camper: ")
                estado=input("ingrese el estado del camper: ")
                riesgo=input("ingrese el riesgo del camper: ")
                nuevoCamper={
                "nombre":nuevoNombre,
                "apellido":nuevoApellido,
                "direccion":nuevaDireccion,
                "acudiente":nuevoAcudiente,
                "telefono":nuevoTelefono,
                "estado":estado,
                "riesgo":riesgo
            }
                data["campers"].append(nuevoCamper)
                with open("data.json", "w") as file:
                 json.dump(data, file, indent=4)
                print(f"{nuevoCamper} ha sido agregado a la lista de campers.")

        elif opcion == "3":
            with open("data.json","r") as file:
                data=json.load(file)
            campers=data.get("campers",[])
            if campers:
                nombreCamper = input("Ingrese el nombre del camper que desea modificar: ")
                camperEncontrado=None
                for camper in campers:
                    if camper["nombre"]==nombreCamper:
                        camperEncontrado=camper
                        break
                if camperEncontrado:
                    nuevoNombre=input("ingrese el nuevo nombre para el camper: ")
                    camperEncontrado["nombre"]=nuevoNombre
                    
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                    print(f"nombre de {nombreCamper} modificado a {nuevoNombre}.")
                else:
                    print("Camper no encontrado.")
            else:
                print("No hay campers registrados.")


        elif opcion == "4":
            print("Volviendo al menú principal.")
            break

 
