def suma(a,b):
    return a + b

suma(1,2) #Esto no nos devuelve nada

#Para que nos lo devuelve hay que asociar la función a una variable
resultado = suma(1,2)
print(resultado)

#Ejemplo práctico
def full_name(first,last):
    return f'{first} {last}'

jon = full_name('Jon','Madariaga')

def saludo(name):
    print(f'Hola {name}, ¡bienvenido!')


saludo(jon)

#Si usasemos print(), al no devolver un valor, nada se almacenaría en la variable 'jon' por lo que devolvería None.
def full_name(first,last):
    print(f'{first} {last}')

jon = full_name('Jon','Madariaga')

def saludo(name):
    print(f'Hola {name}, ¡bienvenido!')


saludo(jon)
