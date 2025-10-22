nombres = ["Ana", "Antonio", "Ana", "Jose", "Carlos"]
# Agregar al final
nombres.append("Aby")
print(nombres)
# insertar en una posicion
nombres.insert(int(input("posicion: ")), input("Nombre Nuevo: ")) # si coloco un -1 lo que ocurre es que el -1 es igual al numero ultimo de la lista
print(nombres)
# Reemplazar
posicion = int(input("Posicion: "))
nombres[posicion] = input("Nombre nuevo: ")
print(nombres)
# Quitar el valor de un numero
nombres.remove("Carlos")
print(nombres)
# Borrar segun posicion
nombre_borrado = nombres.pop(3)
print(f"Nombre borrado: {nombre_borrado}")
print(nombres)
# imprimir listas al reves
nombres.reverse()
print(nombres)