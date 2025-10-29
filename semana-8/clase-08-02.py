# voy a iniciar mi variabl en true
ejecucion = True

while ejecucion:
    opcion = input("Estamos ejecutando el menu? Y/N: ")
    if opcion.lower() == "n":
        ejecucion = False
    elif opcion.lower() == "y":
        print("Ok, continuemos.")
    else:
        print("la opcion elegida no es valida")


print("Gracias por utilizar nuestro sistema!!!")
        