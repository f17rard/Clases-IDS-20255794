                                            #Parametro por defecto
def describir_mascota(nombre_mascota: str, tipo_animal: str="perro"): #los parametros por defecto van en al final de la función
    """Esta funcion  describe una mascota"""
    print(f"mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"y es un {tipo_animal.lower()}")
    
# describir_mascota(tipo_animal="perro", nombre_mascota="phoenix") #definir parametros
# describir_mascota("rufus") #no coloco el segundo parametro, ya que ahora es un parametro predefinido

def registro_usuario(nombre, apellido, inicial="", edad=0): #funcion para decidir que hacer si faltan parametros
    """Constuir un nombre a partir de sus componentes"""
    if edad and inicial:
        texto_completo = f"La persona {nombre.capitalize()} {inicial.upper()}. {apellido.capitalize()}, de {edad} años de edad."
    elif inicial:
        texto_completo = f"La persona {nombre.capitalize()} {inicial.upper()}. {apellido.capitalize()}."
    elif edad:
        texto_completo = f"La persona {nombre.capitalize()} {apellido.capitalize()}, de {edad} años de edad"
    else:
        texto_completo = f"La persona {nombre.capitalize()} {apellido.capitalize()}."
        
    print(texto_completo)
    
# registro_usuario("juan", "gavidia", "w", 35)

def saludar_usuario(nombres): #trabajo con lista 
    """Saludar al usuario"""
    for nombre in nombres:
        print(f"Hola {nombre.capitalize()}")

usuarios = ["alvin", "ana", "LUIS"]
saludar_usuario(usuarios)