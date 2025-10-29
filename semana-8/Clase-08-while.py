presupuesto = 1000
gasto = 0

while gasto < presupuesto:
    compra = float(input("monto a comprar: "))
    gasto += compra

if presupuesto < compra:
    print(f"el monto gastado es de: ${gasto}")
    print("te falta dinero")
    print(f"el monto faltante es de: ${gasto-presupuesto}")
else:
    print("has llegado al limite del presupuesto")
    print(f"el monto gastado es de: ${gasto}")