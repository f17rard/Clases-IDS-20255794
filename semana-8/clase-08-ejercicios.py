"""#ejercicio
valores = [[1, 3, 6],
           [2, 7, 4],
           [6, 5, 9],
           [1, 10, 20]]

lista = []
n = int(input())

for i in valores:
    for v in i: #entrar a los elementos de los elementos - Alvin 2025
        if v > n:
            lista.append(v)

print(lista)
"""

#ejercicio 2
valores = [[1, 3, 6],
           [2, 7, 4],
           [6, 5, 9],
           [1, 10, 20]]

valor = 0

for v in valores:
    for i in v:
        while valor != 45:
            valor += i
            
        
print(valores[v][i])