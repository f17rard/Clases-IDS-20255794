#Ejercicio 1 - Registro de clientes
clientes = {}

def registro(): #funcion para llamar el registro de cliente
    conteo = 0
    while conteo !=2:
        dui = input("Digite su DUI: ")
        if len(clientes) == 0:
            if len(dui) == 10 and dui[-2] == "-": #comprobar que está correcto el dui
                conteo = 2
            else:
                print("Su DUI no cuenta con los parametros correctos")
        else:
            for i in clientes.keys():
                if dui == i:
                    print("El DUI escrito ya se encuentra registrado.")
                    conteo = 0
                elif len(dui) == 10 and dui[-2] == "-": #comprobar que está correcto el dui
                    conteo = 2
                    break
                else:
                    print("Su DUI no cuenta con los parametros correctos")

    nombre = input("Escriba su nombre: ")
    apellido = input("Escriba su apellido: ")
    print("")
    clientes[dui] = f"{nombre} {apellido}"


while True:
    menu = input(f"""Seleccione una opcion
    1. Registrarse
    2. Consultar clientes
    3. Salir
    Digite: """)
    print("")

    if menu == "1":
        registro()
    elif menu == "2":
        if len(clientes) == 0:
            print("No se ha registrado ningun cliente. \n")
        else:
            for d, n in clientes.items():
                print(f"{d.capitalize()}: {n.title()}")
            print("")
    elif menu == "3":
        break
    else:
        print("el numero no es valido. \n")
