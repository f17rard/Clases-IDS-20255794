#Ejercicio 1 - Registro de clientes
clientes = {}
servicios = {"WD":"Diseño web", 
             "DS":"Ciencia de datos", 
             "ML":"Machine learning aplicado", 
             "API":"Desarrollo de APIs Empresariales"}
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
        nombre = input("Escriba su nombre: ")
        if len(nombre) < 2:
            print("Debe escribir un nombre valido.")
        else:
            break
    
    while True:    
        apellido = input("Escriba su apellido: ")
        if len(apellido) < 2:
            print("Debe escribir un apellido valido.")
        else:
            break
           
       
    clientes[dui] = f"{nombre.capitalize()} {apellido.capitalize()}"
    print("El cliente fue registrado con exito.")
    print("")
    
def contratar_servicio():
    while True:
        if len(clientes) == 0:
            print("No hay clientes registrados.")
            print("Si desea contratar un servicio por favor regístrese.")
            break
        else:
            solicitud = input("""Digite su DUI para hacer una solicitud
                              (si desea salir escriba "salir"): """)
            if solicitud.capitalize() == "Salir":
                break
            else:
                for i in clientes.keys():
                    if solicitud == i:
                        print("a")
                        
                    
        

while True:
    menu = input("""=========== MENU ===========
    1. Crear usuario
    2. Contratar servicio
    3. Listar clientes por servicio
    4. Salir
    Seleccione una opcion: """)

    if menu == "1":
        crear_cliente()
        for d, n in clientes.items():
            print(d, n)
    elif menu == "4":
        break
    else:
        print("Digite una opción correcta.")