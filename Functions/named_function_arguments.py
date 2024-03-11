'''
Si tenemos una función que contiene muchos argumentos, la opción posicional
nos puede llevar a errores. Por lo que la mejor opción es explicitar cuál es 
el valor de cada argumento para omitir esa característica posicional.
'''

def saludar(nombre, saludo = '¡Hola'): #Primer argumento nombre y segundo saludo
    print(f'{saludo} {nombre}!')


saludar(saludo = 'Bienvenido', nombre = 'Jon') #Hemos alterado el orden de los argumentos y aún asi funciona