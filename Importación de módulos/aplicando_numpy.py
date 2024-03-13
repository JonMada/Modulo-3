#Ejercicio para obtener listas anidadas partiendo de una lista
#[1,2,3,4,5,6...] --> [[1,2],[3,4],[5,6]...]
import numpy as np
num_range = np.arange(16) #Nos devuelve una matriz de 16 elementos
print(num_range) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
num_range= np.reshape(num_range, (4,4)) #La función reshape() devuelve un nuevo arreglo que contiene los mismos datos que el arreglo original, pero con la forma especificada.
print(num_range) #Nos devuelve un array con matrices anidadas 4x4
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]] 
'''

