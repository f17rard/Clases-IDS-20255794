#Ejercicio-1: configuración inicial
agente = "Encargado"
platillo = []
precios = []

#Ejercicio-2: Ingreso a la aplicación
a= input("Ingrese el nombre del agente: ").lower()
while a != agente.lower():
    print("Agente no registrado")
    a = input("Favor ingrese el nombre del agente: ").lower()

#Ejercicio-3: Gestion del menú principal
accion = True
while accion:
    menu = input("Seleccione una opcion: (1: Creacion de platillos, 2: Consulta de platillos y precio, 3: Colocar un pedido, 4: Salir): ")
    
    if menu == "1": #Ejercicio-4: Creacion de platillos 
        plato = input("Ingrese el nombre del platillo a crear: ").capitalize()
        precio = float(input("Ingrese el precio del platillo a crear: "))
        platillo.append(plato)
        precios.append(precio)
    elif menu == "2": #Ejercicio-5: Consulta de platillos
        if len(platillo)==0 and len(precios)==0:
            print("Actualmente no hay platillos ingresados")
        else:
            for i in range(len(platillo)):
                print(f"{platillo[i].capitalize()}: ${precios[i]:.2f}")
    elif menu == "3": #Ejercicio-6: Colocar un pedido
        salida = True
        while salida:
            pedido = input("Indique el nombre del platillo para su orden: ")
            if platillo.count(pedido.capitalize()) == 1:
                N = platillo.index(pedido.capitalize())
                print(f"Usted ha elegido {platillo[N].capitalize()} con un precio de ${precios[N]:.2f}")
                salida = False
            else:
                print("El platillo no existe")
                salida = True
    elif menu == "4": #Ejercicio-7: Salir
        accion = False
    else:
        print("seleccione una opcion correcta")

