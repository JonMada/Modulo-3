#Antes de nada conviene explicar el desempaquetado extendido para entender el flujo de trabajo de la función:

a, b, c = [1,2,3] #Nos permite desempaquetar cada elemento y asignarlo a las variables 'a', 'b' y 'c'.

#Pero, ¿qué pasaría si la lista es más extensa que las variables de asignación?

# a, b, c = [1,2,3,4,5] #Nos devolvería error

#La solución es aplicar '*' para que una de las variables englobe lo restante

a, *b, c = [1,2,3,4,5]
print(a) #1
print(b) #[2, 3, 4]
print(c) #5

*a, b, c = [1,2]
print(a) #[1,2,3]
print(b) #4
print(c) #5


#Ejercicio: 

def borrador_primer_segundo_elemento(mi_lista):
    if len(mi_lista) >3:
        _, *content, _ = mi_lista
        print(content)
    else:
        print('Error. Necesitamos una lista con más de 3 elementos')

html = ['<h1>' , 'Hola', 'mundo', '</h1>']

borrador_primer_segundo_elemento(html)

