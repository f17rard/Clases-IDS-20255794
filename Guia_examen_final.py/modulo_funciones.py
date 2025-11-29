#Definir funciones para el modulo main
from modulo_datos import estudiantes, cursos, inscripciones

def registar_estudiantes():
    """Funcion que valida y registra estudiante"""
    
    while True: #captura de carnet
        carnet_i = input("Digite el número de su carnet: ")
        compro = False
        
        for c in estudiantes:
            if c["carnet"] == carnet_i: #verifico si el carnet existe
                compro = True
                break
            
        if compro: #informo que el carnet existe
            print("El carnet existe. Registre uno diferente.")
        elif 6<= len(carnet_i) <=10: #compruebo los requisitos
            break
        else:
            print("el largo del carnet debe ser mayor a 5 y menor a 11.")
        
            
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
    while activador:
        carnet_c = input("Digita tu carnet (si deseas salir escribe 'salir'): ")
        #si escribe salir
        estado = True
        if carnet_c.lower() == "salir":
            print("Saliendo...")
            activador = False
            break
        else:
            for c in inscripciones:
                if carnet_c == c[0]: #comprobando si esta en un curso
                    print("Ya esta inscrito en un curso.")
                    estado = False
                    existe = True
                else:
                    print("Digite un carnet.")
                break
                
        
        existe = False
        while estado:
            for i in estudiantes: 
                if carnet_c == i["carnet"]:
                    print("Seleccione un curso.")
                    opcion = input(
                        """Codigo |Descripcion
                PY      |Python básico
                JS      |Javascript para principiantes
                BD      |Introduccion a base de datos
                SE      |Seguridad de entornos digitales
                        
                Digite el codigo del curso que desea cursar
                        (Si quiere salir escriba salir): """
                    ).upper()
                    if opcion in cursos.keys():
                        print("Registado.")
                        inscripciones.append(
                            (carnet_c, opcion)
                        )
                        estado = False
                        existes = True
                    elif opcion == "SALIR":
                        estado = False
                    else:
                        print("Seleccione una opcion valida")
                    existe = True
                    break
        
        if existe == False:
            print("No exites.")
            
                
        
def generar_reporte():
    while True:
        if len(inscripciones) == 0: #Si no hay nadie inscrito
            print("No se ha realizado ninguna inscripción.")
            break
        
        if len(inscripciones) > 0: #Aqui si encuentra gente inscrita.
            menu2= input(
                """-- Menu de reportes --
                1. PY
                2. JS
                3. BD
                4. SE
                5. Estudiantes sin inscripciones
                6. Salir
                
                Seleccione una opcion: """
            )
            if menu2 == "1": #aqui se comprueba si hay gente en Python
                for a, i in enumerate(inscripciones, start=1):
                    if i[1] == "PY":
                        print(a, i[0])
                    else:
                        print("no hay nadie")
                        break
            elif menu2 == "5":
                for c in enumerate(estudiantes, start=1):
                    for a, i in enumerate(inscripciones, start=1):
                        if i[1] != c["carnet"]:
                            print(a, c[0])
                        else:
                            print("no hay nadie")
                            break
            elif menu2 == "6":
                break