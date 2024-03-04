#Estructura básica de un set:
mi_set = {1,2,3,4,5}

#Transformar cualquier estructura de datos en un set --> 'set()' function
mi_lista = [1,2,3,4,5]
mi_lista_transformada_en_set = set(mi_lista)
print(mi_lista_transformada_en_set)

#Operaciones con sets:
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

#Unión de conjuntos:
union = set_1 | set_2
print(union)

#Intersección de conjuntos:
interseccion = set_1 & set_2
print(interseccion)

#Diferencia de conjuntos:
diferencia_2 = set_1 - set_2
print(diferencia_2)

