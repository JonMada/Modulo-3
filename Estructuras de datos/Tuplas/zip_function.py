nombres = ['Juan', 'María', 'Pepe']
edades = [29,78,32]

datos_combinados = zip(nombres,edades)
print(list(datos_combinados))


lista1 = [1,2,3,4,5]
lista2 = ['a','b','c','d','e']
listas_combinadas = zip(lista1,lista2)
print(listas_combinadas) #Esto nos devuelve un zip object

#Aparte del recurso 'list' podemos crear esta función para que se visualicen
for elementos in listas_combinadas:
    print(elementos)

