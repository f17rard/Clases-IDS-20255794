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

palabra = "tratar"

print(palabra==palabra[::-1])