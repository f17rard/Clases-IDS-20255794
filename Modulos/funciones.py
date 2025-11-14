#Este modulo contendrá las funciones

def registro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesores, utilizando kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias:")
    
    for ciclo, materia in materias.items():
        print(f"\t - {ciclo}: \t {materia}")
        
def ordenar_pizza(size, *ingredientes): #ahora con args
    """Vamos a imprimir su orden"""
    print(f"usted ha ordenado una pizza {size} de:") 
    for i in ingredientes:
        print(f"\t- {i}")


def saludar_usuario(nombres): #trabajo con lista 
    """Saludar al usuario"""
    for nombre in nombres:
        print(f"Hola {nombre.capitalize()}")