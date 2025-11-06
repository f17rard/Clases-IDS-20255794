#iteraciones de listas

# surnames = ["Rivest", "Shamir", "Adleman"]
# for position, surname in enumerate(surnames, start=1):
#     print(position, surname)

lista1 = ["Nick", "Rick", "Roger", "Syd"]
edad = [23, 45, 18, 21]
frutas = ["manzana", "pera", "piña", "uva"]
deportes = ["Futbol", "Basketball", "Natacion", "Baseball"]
for person, age, fruta, deporte in zip(lista1, edad, frutas, deportes):
    print(person, age, fruta, deporte)
#uno decide que hacer con los datos

