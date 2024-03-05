#Ejemplos básico:

#Queremos a partir de la lista 'numbers' crear una resultados en la que a cada elemento añadido se le sume +1
numbers = [1,2,3,4,5,6]
results = [num + 1 for num in numbers] #Esta es la estructura de list comprenhension
print(results)

#Queremos una lista generada a partir de un rango(10) en la que sólo se recogan los elementos pares
num_list = range(1,11)
pares = [num for num in num_list if num % 2 == 0] #Si se cumple la condición de que el resto de ese numero/2 es 0 (par)
'''
Es lo mismo que:
for num in num_list:
    pares.append(num % 2 == 0)
'''
print(pares)

#Ejercicio más avanzado:
num_list = range(1,11)
cubed_nums = [num ** 3 for num in num_list] #Lista de números de 'num_list' elevadas al cubo
'''
Lo anterior es lo mismo que:
for num in num_list:
    cubed_nums.append(num**3)
'''
print(list(num_list))
print(cubed_nums)