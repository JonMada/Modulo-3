#While:
'''
El loop se ejecutará mientras la condición determinada
por 'while' sobre la variable iterable se cumpla. En el momento
en el que se deje de cumplir el bucle se detendrá.
'''
contador = 0

while contador < 5:
    print('El contador es igual a', contador)
    contador +=1

#Ejemplo 2
nums = list(range(1,10)) #Creamos una lista con número llamada 'nums'

while len(nums) > 6: #Mientras la longitud de la lista sea mayor de 50
    print(nums.pop()) #Imprime el último número de la lista en cada iteración



#Adivinador:
def adivinador():
    while True:
        print('¿Qué número crees que es?')
        guess = input()

        if guess == '42':
            print('¡Los has adivinado!')
            return False
        else:
            print(f'Lo siento, {guess} no es el número correcto')

adivinador()


#Ejemplo 3
def print_nombres_perro():
    nombres_de_perro = ['Bruce','Connor','Kaiser','Bizkor']
    counter = 0 
    while counter < 4:
        print(nombres_de_perro[counter])
        counter +=1

print_nombres_perro()

