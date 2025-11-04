birthdays = {
    "Alice" : "Apr 1",
    "Bob" : "Dec 12",
    "Carol": "Mar 4"
}

birthdays["Carol"] = "abr 21" #modificar datos de una clave
birthdays ["Fer"] = "Mar 3" #si la clave no existe, la crea

for persona, fecha in birthdays.items():
    print(f"El cumpleaños de {persona} es en {fecha}")

del birthdays["Bob"] #Borrar una clave
