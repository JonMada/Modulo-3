#Utilizamos la función reduce del paquete functools

import functools

num_list = [1,2,3,4,5,6]

def media_lista (list):
    reduccion= functools.reduce(lambda total, elemento: total + elemento, list)
    print(reduccion / len(list))

media_lista(num_list)


