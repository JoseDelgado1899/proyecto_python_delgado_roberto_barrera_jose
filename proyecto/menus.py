from campers import gestionCampers  
from coordinador import menu_principal

def menuPrincipal():
    while True:
        print("--------------------------------------------------------")
        print("")
        print("              bienvenido a campuslands                   ")                  
        print("")
        print("--------------------------------------------------------")
        print("1. Campers")
        print("2. Trainers")
        print("3. Coordinador")
        print("4. Salir")
        opc=input("seleccione una opcion: ")
        if opc=="1":
            menuCampers()
        if opc=="2":
            menuTrainers()
        if opc=="3":
            menuCoordinador()
        if opc=="4":
            print("saliendo del programa")
            break

def menuCampers():
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
        
        opc = input("Seleccione una opción: ")

        if opc == "1":
            gestionCampers()
        elif opc == "2":
            gestionCampers()  
        elif opc == "3":
            gestionCampers()  
        elif opc == "4":
            break 
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
def menuTrainers():
            opcion=input("seleccione una opcion: ")
            if opcion == "2":
                while True:
                    print("--------------------------------------------------------")
                    print("")
                    print("                   Menú Trainers")
                    print("")
                    print("--------------------------------------------------------")
                    print("1. ver campers asignados a su ruta")
                    print("2. Ver listado de campers")
                    print("3. ver horarios de clases")
                    print("4. Volver al menú principal")

                    opc = input("Seleccione una opción: ")

                    if  opc == "1":
                        gestionCampers()  
                    elif opc == "2":
                        gestionCampers()  
                    elif opc == "3":
                        gestionCampers()
                    elif opc == "4":
                     break 
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
def menuCoordinador():
       
            while True:
                print("--------------------------------------------------------")
                print("")
                print("                   Menú coordinador")
                print("")
                print("--------------------------------------------------------")
                print("1. registrar camper")
                print("2. asignar notas al camper")
                print("3. asignar ruta al camper")
                print("4. volver al menu principal")
                opc = input("Seleccione una opción: ")
                if   opc == "1":
                    gestionCampers()
                elif opc == "2":
                    menu_principal()
                elif opc == "3":
                    gestionCampers()  
                elif opc == "4":
                    break 
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
            
