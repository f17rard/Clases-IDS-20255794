# un pequeño sistema de registro de alumnos

#configuracion inicial
alumnos = 0
lista_alumnos = []

print("Bienvenido a nuestro sistema de control de Alumnos.")
menu_activo = True

while menu_activo:
    opcion = input("Elija la opcion (1: Ingresa alumno, 2: Consultar, 3: Modificar, 5: Salir): ")
    if opcion == "5":
        menu_activo = False
    elif opcion == "1":
        alumno = input("nombre del alumno agregar: ")
        lista_alumnos.append(alumno)
    elif opcion == "2":
        print(lista_alumnos)
    elif opcion == "3":
        n = int(input("Ingrese la posicion del alumno a modificar (1-4): "))
        a = input("ingrese el nuevo nombre del alumno: ")
        lista_alumnos[n-1] = a

print("Gracias por utilizar nuestro sistema.") 