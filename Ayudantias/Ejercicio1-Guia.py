"""#Ejercicio 1
num = float(input())

if num>=0 :
    print("Positivo")
else:
    print("Negativo")
"""

"""#Ejercicio 2
num= int(input())

if num%2 == 0:
    numS= num+2
    numA= num-1
    print(numS)
    print(numA)
else:
    numS= num+1
    numA= num-2
    print(numS)
    print(numA)
"""

"""#Ejercicio 3
nota1=float(input())
nota2=float(input())
nota3=float(input())
nota4=float(input())
nota5=float(input())
nota6=float(input())

prom = (nota1+nota2+nota3+nota4+nota5+nota6)/6

if prom>9.5:
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")
"""

"""#Ejercicio 4
rep=int(input())
lista = []

for c in range(rep):
    num = int(input())
    lista.append(num)

print(f"{lista.count(7)} {lista.count(5)}")
"""

"""#ejercicio 5
Ncombos = int(input())
pa, pb, pc = map(int, input().split())
damageT = []

for i in range(Ncombos):
    combo = input().upper()
    daño = (combo.count("A")*pa)+(combo.count("B")*pb)+(combo.count("C")*pc)
    damageT.append(daño)

for i in range(Ncombos):
    print(damageT[i])
"""

"""#Ejercicio 6
n = int(input())
lista_nombres = []

for i in range(n):
    nombre = input()
    if len(nombre)<=6:
        lista_nombres.append("No vale la pena")
    elif len(nombre)>= 8:
        lista_nombres.append("Si aguanto otro desarrollo de personaje")
    elif len(nombre)>6 and len(nombre)<8:
        lista_nombres.append("Dios no creo aguantar esta vez")

for i in range(n):
    print(lista_nombres[i])

"""

"""#Ejercicio 7
num1, num2 = map(int, input().split())

if num1>num2:
    print(num1)
else:
    print(num2)
"""

"""#Ejercicio 8
n = int(input())
entra = 0

for i in range(n):
    edad = int(input())
    if edad>=15:
        entra = entra + 1
    else:
        entra = entra

print(entra)
"""

"""#ejercicio 9
estado = input().lower()

if estado == "conectado":
    print("Ola Ivan")
elif estado == "desconectado":
    print("Ol...")
"""

"""#Ejercicio 10
n = int(input())
lista = []
for i in range(n):
    pi = int(input())
    if pi>=3:
        lista.append("Ok")
    else: 
        lista.append("No")

for i in range(n):
    print(lista[i])
"""