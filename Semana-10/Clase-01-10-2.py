#atender pedidos de pizza
                #tratar el valor del parametro como lista
def ordenar_pizza(size, *ingredientes): #ahora con args
    """Vamos a imprimir su orden"""
    print(f"usted ha ordenado una pizza {size} de:") 
    for i in ingredientes:
        print(f"\t- {i}")
    
ordenar_pizza("grande", "queso", "jamon", "peperoni")