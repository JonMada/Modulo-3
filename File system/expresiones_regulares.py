#Expresiones regulares para listar tipos de archivos

#Creamos los archivos
open('something.txt', 'w+')
open('something2.txt', 'w+')
open('config.yml', 'w+')
open('scripts.rb', 'w+')

#Importamos librerías
import fnmatch
import os

#Creamos la función
def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'): #Si el file contiene '.txt' = True -> print file
            print('Text file:', file)
        elif fnmatch.fnmatch(file, '*.rb'):
            print('Ruby file:', file)
        elif fnmatch.fnmatch(file, '*.yml'):
            print('Yaml file:', file)
        elif fnmatch.fnmatch(file, '*.py'):
            print('Python file:', file)

#Llamos a la función:
list_files()       


#La librería fnmatch es aplicable a otros elementos, como pueden ser las listas

from fnmatch import fnmatchcase

jugadores = ['Williams DL', 'Guruzeta DL', 'Vivian DF', 'Paredes DF', 'Sancet MC']

delanteros = [ jugador for jugador  in jugadores if fnmatchcase(jugador, '*DL') ]

print(delanteros) #Nos crea una lista con los delanteros --> ['Williams DL', 'Guruzeta DL']
