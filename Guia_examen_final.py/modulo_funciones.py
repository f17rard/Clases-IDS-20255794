#Definir funciones para el modulo main
from modulo_datos import estudiantes, cursos, inscripciones

def registar_estudiantes():
    """Funcion que valida y registra estudiante"""
    while True: #captura de carnet
        carnet_i = input("Digite el número de su carnet: ")
        compro = False
        for c in estudiantes:
            if c["carnet"] == carnet_i:
                print("El carnet existe. Registre uno diferente.")
                compro = True
        if len(carnet_i)>=6 and len(carnet_i)<=10 and compro == False:
            break
        else:
            print("""No cumple los requisitos. 
- Debe tener más de 5 caracteres y menos de 11. 
- No debe existir el carnet.""")
                
            
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
    
    estudiantes.append(
        {
            "carnet":carnet_i,
            "Nombre": nombre_i.capitalize(),
            "Apellido": apellido_i.capitalize()
        }
    )
    for k in estudiantes:
        print(k)
        
def inscribir_en_curso():
    activador = True
    compro = False
    while activador:
        carnet_c = input("Digite su carnet (Si desea salir escriba 'salir'): ")
        for i in inscripciones:
            if carnet_c == i["carnet"]:
                print("Ya te encuentras inscrito en un curso.")
                compro = True
        for c in estudiantes:
            if carnet_c == c["carnet"] and compro == False:
                while True:
                    print("Cursos disponibles")
                    print("Codigo | Descripcion")
                    print(f"PY     | {cursos['PY']}")
                    print(f"JS     | {cursos['JS']}")
                    print(f"BD     | {cursos['BD']}")
                    print(f"SE     | {cursos['SE']}")
                    code = input("Escriba el codigo del curso que cursará: ").upper()
                    if code == "PY" or code == "JS" or code == "BD" or code == "SE":
                        inscripciones.append(
                            {carnet_c, code}
                        )
                    else: 
                        print("seleccione una opcion corecta")
                
                activador = False
                break
            else:
                print("El carnet no existe o ya estas en un curso")
        if carnet_c.lower() == "salir":
            print("Saliendo...")
            activador = False