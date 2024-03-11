#Estructura básica

def saludo(*args): #'args' es la convención para nombrar los argumentos comprimidos de una función
    print('Hi ' + ' '.join(args))
    print(args) #Nos empaqueta losa argumentos en tuplas


saludo('Jon') #Hi Jon
saludo('Jon', 'Madariaga') #Hi Jon Madariaga
saludo('Jon', 'Madariaga', 'Ortega') # Hi Jon Madariaga Ortega

#Nuestra función puede tomar mas de un argumento, más alla de los empaquetados en 'args'

def saludo(momento_día, *args):
    print(f'Hola {' '.join(args)}! Espero que estes teniendo una bonita {momento_día}.')
    #Hola Jon Madariaga Ortega! Espero que estes teniendo una bonita mañana


saludo('mañana', 'Jon', 'Madariaga','Ortega') #
