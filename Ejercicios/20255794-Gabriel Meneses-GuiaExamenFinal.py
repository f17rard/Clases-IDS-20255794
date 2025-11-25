#Ejercicio 1 - Registro de clientes
clientes = {}
servicios = ["Diseño web", "Ciencia de datos", "Machine learning aplicado", "Desarrollo de APIs Empresariales"]
contratos = {}


def crear_cliente(): #funcion para llamar el registro de cliente
    conteo = 0
    while conteo !=2:
        dui = input("Digite su DUI: ")
        if len(clientes) == 0:
            if len(dui) == 10 and dui[-2] == "-": #comprobar que está correcto el dui
                conteo = 2
            else:
                print("Su DUI no cuenta con los parametros correctos.")
        else:
            for i in clientes.keys():
                if dui == i:
                    print("El DUI escrito ya se encuentra registrado.")
                    conteo = 0
                elif len(dui) == 10 and dui[-2] == "-": #comprobar que está correcto el dui
                    conteo = 2
                    break
                else:
                    print("Su DUI no cuenta con los parametros correctos.")
    
    while True:
        try:
            nombre = input("Escriba su nombre: ")
        except:
            print("\n Tiene que escribir un nombre en el apartado.")
        else:
            break
    
    while True:    
        try:
            apellido = input("Escriba su apellido")
        except:
            print("\n Tiene que escribir un apellido en el apartado.")
        else:
            break
    
    clientes[dui] = f"{nombre.capitalize()} {apellido.capitalize()}"

menu = input("""Menu
            1. Crear usuario
            2. Contratar servicio
            3. Listar clientes por servicio
            4. Salir
            Seleccione una opcion.""")