"""Ejercicio 1

enero=int(input("digite las cantidades de Enero: "))
febrero=int(input("digite las cantidades de Febrero: "))
marzo=int(input("digite las cantidades de Marzo: "))

costos=(enero*1.25+febrero*1.38+marzo*1.14)
#uso de los f-strings
print(f"Las cantidades de enero, febrero y marzo son:" )
print(f"{enero}, {febrero} y {marzo} con un costo")
print(f"de ${costos:.2f}") #.2f es para colocar dos decimales
"""

"""Ejercicio 2, 3

dias=["lunes", "martes", "miercoles", "jueves", "viernes"]

lu= int(input("Lunes: "))
dias[0] = lu
ma= int(input("Martes: "))
dias[1] = ma
mi= int(input("Miercoles: "))
dias[2] = mi
ju= int(input("Jueves: "))
dias[3] = ju
vi= int(input("Viernes: "))
dias[4] = vi
print(dias)
print(f"La produccion de la semana fue: {lu+ma+mi+ju+vi}")
"""

"""Ejercicio 4

alumno = ("Diego", "Franquito", "Clavito", "Aby", "Alvin", "Medranito", "Genesis")

nino= int(input("Ingrese el orden del niño que desea saber (1-7): "))

print(f"El alumno que ingresó como número {nino} es {alumno[nino-1]}") #como mandar a llamar de una tupla
"""

"""Ejercicio 5

nombre=input("Escribe tu nombre: ")
apellido=input("Escribe tu apellido: ")

print("Estas son las propuestas que se le brindan: ")
print(f"propuesta 1: {nombre.lower()}.{apellido.lower()}@ISDN.com")
print(f"propuesta 2: {nombre[0].lower()}.{apellido.lower()}@ISDN.com")
"""

"""#Ejercicio 6

salario = input("Ingrese su salario: ")
print(salario[0]=="$")
print(salario.count("$")==1) #cuenta el numero de veces que se repite "$" en el string
"""

"""#Ejercicio 7

palabra_encriptada="DFGUPCCBJKAJ"

print(palabra_encriptada[0::3])
"""

"""#ejercicio 8

x=10
y=10
print(x != y)
"""

"""#ejercicio 9

import calendar
from datetime import datetime
fecha=datetime.now()
mes = fecha.month
anio_actual = 2025
anio_nacimiento = int(input("digite su año de nacimiento: "))
mes_nacimiento = int(input("digite el número del año de nacimiento: "))
if mes < mes_nacimiento:
    mes_restar = mes_nacimiento-mes
    print(f"Te faltan {mes_restar} mes para cumplir años")
    print(f"Tu edad es de: {(anio_actual-anio_nacimiento)-1}")
else:
    print(f"tu edad es de: {anio_actual-anio_nacimiento}")

"""