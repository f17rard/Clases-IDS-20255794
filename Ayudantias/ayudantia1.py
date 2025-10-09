# num1 = int, input()
# if num1 == int:
# num2 = int, input()


######################Ejercicio 2#########################################

# a, b = map(int, input().split())
# print(a+b)

####################Ejercicio 3######################################
#el while no necesita usar un "else:"

num_manzana = int(input())
cliente = 0

while num_manzana != 1: 
    cliente_final=cliente+1
    if num_manzana%2 == 0:
        num_manzana = num_manzana/2
        print(num_manzana)
    else:
        num_manzana = (num_manzana*3)+1
        print(num_manzana)

print(cliente_final)
