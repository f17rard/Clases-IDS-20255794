#funciones usando kwargs
#args = * y kwargs = **

def registro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesores, utilizando kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias:")
    
    for ciclo, materia in materias.items():
        print(f"\t - {ciclo}: \t {materia}")

registro_profesores(
    "Alvin",
    "Portillo",
    ciclo1 = ["BD1", "IIJ", "A&GD"],
    ciclo2 = ["DAI", "BD2", "SINE"],
    ciclo3 = ["IDS", "FPEN", "PAD"]
)