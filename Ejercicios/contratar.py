diccionario = {"1": "hola",
               "2": "Hola", #
               "3": "hola",
               "4": "Hola", #
               "5": "hola",
               "6": "Hola",}#

diccionario2 = {"2": "hola",
                "4": "hola",
                "6": "hola",}

no = []

for k, v in diccionario.items():
    if v == "Hola":
        print(k)
print("")
for k in diccionario.keys(): #quiero que imprima 1, 3 y 5
        if k not in diccionario2:
            print(k)
                