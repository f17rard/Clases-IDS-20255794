semana = {}
semana["uno"] = "Lunes"
semana["dos"] = "Martes"
semana["tres"] = "Miercoles"
semana["cuatro"] = "Jueves"
semana["cinco"] = "Viernes"
print(semana)
# La relacion "clave: valor" es un "item"
#Keys()   |
#Values() | secuencia / iterable
#Items()  |

for k, v in semana.items():
    print(f"El dia {k} de la semana es {v}.")
# lo que hace item es crear dos listas en base al diccionario 