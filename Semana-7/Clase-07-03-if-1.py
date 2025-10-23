# Por fin TT
numero = 6

captura = int(input("Adivina el numero (un intento): ")) 

if captura == numero: # todo lo que este fuera del tabulador esta fuera de la condicional if
    print("Adivinaste el numero!!!!!") # esto esta dentro de if
else: # else se ocupa para usar el false de la operacion booleana
    print("El numero es incorrecto, gua gua :(")
print("Puedes seguir jugando.") # esto esta fuera de if