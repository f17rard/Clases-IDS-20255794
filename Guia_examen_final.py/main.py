#El menu de mi sistema donde llamare las funciones de los modulos 

#Importar modulos a usar
from modulo_funciones import registar_estudiantes, inscribir_en_curso
while True:
    print("""
-- Menú principal -- 
1. Registrar estudiante
2. Inscribir curso
3. Generar reportes
4. Salir
    """)
    opcion = input("Elija una opcion [1-4]: ")
    if opcion == "1":
        registar_estudiantes()
    elif opcion == "2":
        inscribir_en_curso()
    elif opcion == "3":
        print("Elegiste 3")
    elif opcion == "4":
        print("Gracias, vuelva pronto.")
        break
    else:
        print("Selecciona una opcion valida.")