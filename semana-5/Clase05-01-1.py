### Ejercicios sobre tuplas

# una tupla es inmutable
# las listas son mutables


tupla1 = (1,12,255,1289,60,000) #al colocar parentesis se hacen las tuplas
lista1 = [1,12,255,1289,60,000] #los corchetes hacen una lista acá
print(tupla1)
print(len(tupla1))
print(tupla1[3:])
print(lista1)
lista1[-1] = 3 # a las listas se le pueden hacer modificaciones y a las tuplas no

print(lista1) 