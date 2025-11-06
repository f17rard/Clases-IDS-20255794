activado = True
productos = {}
clientes = {}

CodigoP = 0
CodigoC = 0


while activado:
    menu = input("""Elija una opcion:
                 1. Mostrar productos
                 2. Agregar producto
                 3. Registrar nuevo cliente
                 4. Mostrar clientes
                 5. Registrar pedido
                 6. Mostrar pedidos del día
                 7. Mostrar categorias disponibles
                 8. Salir
                 Escriba aqui: """)
    if menu == "1":
        print(productos)
    elif menu == "2":
        for i in range(1):
            codigo += 1
            productos[f"P{codigo+1}"]
