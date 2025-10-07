usuario = "Javier"
q_alumnos = 79
edad_promedio = 18.231234
monto_hope = 1234567.5678901
inversion_evento = -98765.21548

# print(type (q_alumnos))
# print(type (edad_promedio))

# print(type(q_alumnos) is int) 
# print(type(edad_promedio) is int)

# print("el usuario es:", usuario, "y tiene", q_alumnos, "alumnos")
# print("la edad promedio es de", edad_promedio)

#f-string
# print(f"El usuario es {usuario}")
# print(f"y en su aula con {q_alumnos - 4} pajaritos en su aula")
# print(f"con la edad promedio de {edad_promedio:.2f} años ") # .2f - dos decimales fijos
# #El dos a la par de la f es el número de decimales que se mandan a imprimir
# print(f"colectaron {monto_hope:,.2f} como un donativo") #la coma llama la función de la coma de cada mil
# print(f"y la totalidad de gasto fue de {abs(inversion_evento):,.2f} dolares.") #abs - valor absoluto

# print(type(usuario) is str)

# esta_lloviendo = False

# print(type(esta_lloviendo)is bool)
# print(type(monto_hope)is not bool)

nombre = "Alvin"
apellido = "Portillo"
nombre_completo = nombre + " " + apellido #se estan "concatenando" dos variables de texto 
print(nombre_completo)

str5 = str(3.1416)
print(type(str5))