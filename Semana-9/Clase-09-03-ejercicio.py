#Ejercicio de clase

def dui_validacion():
    dui = input("Digite su dui: ")
    condiciones = 0
    con1 = len(dui) == 10
    con2 = dui.count("-") == 1
    con3 = len(dui[dui.index("-"):]) == 2
    
    if con1:
        condiciones +=1
        
    if con2:
        condiciones += 1
    
    if con3:
        condiciones +=1
    
    print(f"Cumple {condiciones} condiciones")
    
dui_validacion()
