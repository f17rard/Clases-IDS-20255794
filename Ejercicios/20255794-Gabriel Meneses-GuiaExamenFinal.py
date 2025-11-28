#Ejercicio 1 - Registro de clientes
clientes = {}
servicios = {"WD":"Diseño web", 
             "DS":"Ciencia de datos", 
             "ML":"Machine learning aplicado", 
             "API":"Desarrollo de APIs Empresariales"}
contratos = {}


def crear_cliente(): #funcion para llamar el registro de cliente
    """Funcion para registar un cliente."""
    print("")
    while True:
        dui = input("Digite su DUI: ")
        if dui in clientes:
            print("El DUI ya se encuentra registrado.")
        else:
            if len(dui) == 10 and dui[-2] == "-":
                break
            else:
                print("Su DUI no cumple con los parametros.")
    
    while True:
        nombre = input("Escriba su nombre: ")
        if len(nombre) < 2 or nombre.count(" ") >= 1:
            print("Debe escribir un nombre valido.")
            print(""" - Debe tener más de dos caracteres.
 - No puede tener espacios.""")
        else:
            break
    
    while True:    
        apellido = input("Escriba su apellido: ")
        if len(apellido) < 2 or apellido.count(" ") >= 1:
            print("Debe escribir un apellido valido.")
            print(""" - Debe tener más de dos caracteres.
 - No puede tener espacios.""")
        else:
            break
    print("")
           
       
    clientes[dui] = f"{nombre.capitalize()} {apellido.capitalize()}"
    print("El cliente fue registrado con exito.")
    print("")
    
def contratar_servicio():
    """Funcion para solicitar un servicio."""
    while True:
        if len(clientes) == 0:
            print("no hay clientes registrados.")
            break
        else: #si hay clientes
            ingreso = input("escriba su DUI (si quiere salir, escriba 'salir'): ")
            if ingreso in clientes:
                if ingreso in contratos:
                    print("ya cuenta con un servicio.")
                else:
                    print("Seleccione una opcion: ")
                    print("Codigo | Descripcion")
                    print(f"WD     | {servicios['WD']}")
                    print(f"DS     | {servicios['DS']}")
                    print(f"ML     | {servicios['ML']}")
                    print(f"API    | {servicios['API']}")
                    code = input("Digite el codigo (si quiere salir, escriba 'salir'): ").upper()
                    if code in servicios:
                        contratos[ingreso] = code
                        print("El servicio ha sido contratado.")
                    elif code.lower() == "salir":
                        break
                    else:
                        print("Escriba un codigo valido.")
                break
            else:
                print("El Dui no esta registrado.")
                
def listar_clientes_por_servicio():
    """lista los clientes que hay dentro de un servicio."""
    while True:
        if len(contratos) == 0: #si no hay contratos
            print("No se han realizado contrataciones.")
            break
        else:
            print("Menú de contrataciones")
            print("""    1. WD
    2. DS
    3. ML
    4. API
    5. No contratados
    6. Salir""")
            opcion = input("Seleccione un número: ")
            if opcion == "1":
                print("")
                print(f"= {servicios['WD']} =")
                for k, v in contratos.items():
                    if v == "WD":                        
                        print(k)
            elif opcion == "2":
                print("")
                print(f"= {servicios['DS']} =")
                for k, v in contratos.items():
                    if v == "DS":                                              
                        print(k)
            elif opcion == "3":
                print("")
                print(f"= {servicios['ML']} =")
                for k, v in contratos.items():
                    if v == "ML":
                        print(k)
            elif opcion == "4":
                print("")
                print(f"= {servicios['API']} =")
                for k, v in contratos.items():
                    if v == "API":
                        print(k)
            elif opcion == "5":
                print("")
                print("= No contratados =")
                for k in clientes.keys():
                    if k not in contratos:
                        print(k)
                    else:
                        print("Todos los clientes registrados cuentan con un servicio contratado.")
            elif opcion == "6":
                break

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
            print(f"{d}: {n}")
        print("")
    elif menu == "2":
        contratar_servicio()
    elif menu == "3":
        listar_clientes_por_servicio()
    elif menu == "4":
        print("")
        print("Gracias por ocupar nuestros servicios.")
        print("")
        break
    else:
        print("Digite una opción correcta.")