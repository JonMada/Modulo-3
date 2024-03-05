compradores = ['Valeria', 'Pablo', 'Ésther','Mario']
nuevos_compradores = ['Ane','Álvaro']

#Podriamos pensar que una alternativa para unir ambas listas podría ser:
# compradores = [compradores,nuevos_compradores]
# print(compradores) #[['Valeria', 'Pablo', 'Ésther', 'Mario'], ['Ane', 'Álvaro']]
#Esto nos devuelve una lista con listas dentro, no es lo más óptimo.
#Simplemente ha combinado ambas listas en un elemento lista

#Alternativa loop 'for' 'in'
for nuevo_comprador in nuevos_compradores:
    compradores.append(nuevo_comprador)
#Esto lo que indica es que se añada a compradores cada elemento 'nuevo comprador (nueva cadena)' a través de iteración

print(compradores)


#Ejercicio: de la lista numbers incrementar cada elemento en 1 y añadir resultado a la lista results.
numbers = [1,2,3,4,5,6]
result = []

for num in numbers:
    result.append(num + 1)

print(result)



