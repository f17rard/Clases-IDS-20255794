nombre = "Alvin"
palabra = "reconocer"
otra_palabra = "palabra"

# print(len(nombre)) #Cantidad de elementos que contiene mi estructura

# print(nombre[2]) #imprime la letra que esta asignada al número
# print(nombre[2:5])
# print(nombre[2:]) #genera desde el que se le asignó hasta el último

# #palindro (tengo que verlo luego)

print(len(palabra))
print(palabra[4:])
print(palabra[0::2])
print(palabra[::-1])
print(otra_palabra[::-1])#palabras en inversa

#########################################

# palabra = "tratar"

# print(palabra==palabra[::-1])

# numero = 255
# print(numero)
# print(len(numero)) #los numeros en python no tienen largo


#########################################

mi_palabra = "jocote de corona"
print(mi_palabra)
mi_palabra_mayuscula = mi_palabra.upper() #upper hace el objeto original en texto de minúscula a mayúscula
mi_palabra_cap = mi_palabra.capitalize()
mi_palabra_all_mayus = mi_palabra.title()
print(mi_palabra_mayuscula)
print(mi_palabra_cap)
print(mi_palabra_all_mayus)