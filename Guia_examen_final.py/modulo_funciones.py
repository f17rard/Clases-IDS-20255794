#Definir funciones para el modulo main
from modulo_datos import estudiantes, curso, inscripciones

def registar_estudiantes():
    """Funcion que valida y registra estudiante"""
    while True: #captura de carnet
        carnet_i = input("Digite el número de su carnet: ")
        if len(carnet_i) >= 6 and len(carnet_i) <= 10:
            if carnet_i in estudiantes:
                print("El carnet ya se encuentra registrado.")
            else:
                break
        else:
            print("El carnet debe ser mayor a 5 y menor o igual a 10.")
            
    while True:   
        nombre_i = input("Digite el nombre del estudiante: ")
        if len(nombre_i) > 1:
            break
        else:
            print("El largo del nombre debe ser de al menos 2 caracteres.")
            
    while True:
        apellido_i = input("Digite el apellido del estudiante: ")
        if len(apellido_i) > 1:
            break
        else:
            print("El largo del apellido debe ser de al menos 2 caracteres.")
    
    estudiantes[carnet_i] = [nombre_i, apellido_i]
    for k, v in estudiantes.items():
        print(f"{k}: {v}")
        
def inscribir_en_curso():
    
    