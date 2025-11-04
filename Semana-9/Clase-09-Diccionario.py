#Estructuras de datos - Diccionarios - mutables
#Los diccionarios no funcionan con indices sino con claves
#Se construyen por medio de llaves {}
#SET - referencia: indicie - {} - no permite repetidos - 

#vamos a crear un diccionario 
mi_gato = {
    "nombre": "pelusa",
    "edad": 3, 
    "personalidad": "simpatico"
}
            # {clave : valor}
abys_cat = {
    "personalidad": "simpatico",
    "nombre": "pelusa",
    "edad" : 3
}

copia = mi_gato == abys_cat

print(copia)

