#Este es un docstring de modulo
#Vamos a crear varias funciones

def saludar(): #defincion de funcion
    """Es una funcion que va a saludar"""
    nombre = input("Digite el nombre: ")
    apellido = input("Digite el apellido: ")
    nombre_completo = f"{nombre.upper()} {apellido.upper()}"
    print(f"Hola {nombre_completo}") 
                    #parametro
def saludar_con_param(nombre, apellido): #defincion de funcion
    """Es una funcion que va a saludar"""
    
    print(f"Hola {nombre.title()} {apellido.title()}")
                #argumento

def describir_mascota(animal, nombre_mascota): #las funciones se definen con minusculas
    """Vamos a describir mascotas."""
    print(f"Tengo un {animal}, y su nombre es {nombre_mascota.title()}.")
    
describir_mascota(nombre_mascota="firulais", animal="perro") #puedo asignar valores a los parametros
describir_mascota("gato", "mishito")
describir_mascota(
    input("Digite el tipo de animal: "),
    input("Digite el nombre de la mascota: ")
)