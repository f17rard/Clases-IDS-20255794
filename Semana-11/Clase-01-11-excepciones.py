# def calcular_impuestos():
#     pass


while True:
    try: 
        monto = len(int(input("Digite: ")))
    except TypeError as te: 
        print("Se genera un error de tipo: ", te)
    except ValueError as ve:
        print("es un error de valor:", ve)
    else: 
        impuesto = monto + 25
        print(f"resultado: ${impuesto:,.2f}")
        break
    finally:
        print("Hemos terminado la ejecucion de esta pregunta.")

