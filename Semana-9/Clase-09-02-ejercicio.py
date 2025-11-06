activado = True
productos = []
clientes = {}

codigoP = 0
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
        for i in productos:
            print(i)
    elif menu == "2":
        codigoP += 1
        producto = {}
        if codigoP> 10:
            producto[f"P0{codigoP}"] = input("Ingrese el nuevo producto: ")
            producto["Categoria"] = input("Escriba la categoria del producto: ")
            producto["Precio"] = input("Digite el precio del producto: ")
            productos.append(producto)
        elif codigoP> 100:
            producto[f"P{codigoP}"] = input("Ingrese el nuevo producto: ")
            producto["Categoria"] = input("Escriba la categoria del producto: ")
            producto["Precio"] = input("Digite el precio del producto: ")
            productos.append(producto)
        else:
            producto[f"P00{codigoP}"] = input("Ingrese el nuevo producto: ")
            producto["Categoria"] = input("Escriba la categoria del producto: ")
            producto["Precio"] = input("Digite el precio del producto: ")
            productos.append(producto)
    elif menu == "8":
        activado = False
