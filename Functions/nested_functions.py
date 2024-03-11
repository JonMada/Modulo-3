#Ejemplo práctico

def saludo(first,last):
    def full_name():
        return f'{first} {last}'
    print(f'Hola {full_name()}.¡Bienvenido!')


saludo('Jon','Madariaga')


#Esto es lo mismo que:
def full_name(first,last):
    return f'{first} {last}'

jon = full_name('Jon','Madariaga')

def saludo(name):
    print(f'Bienvenido {name}')


saludo(jon)


#Otro ejemplo de nested functions:
import math

def resultado (num1,num2):
    def operacion():
        return ((math.pow(num1,3)) / num2)
    print(f'El resultado es {operacion()}')

resultado(30,23)