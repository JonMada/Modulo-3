#Keywords arguments:
'''
Nos permite aplicar el empaquetado de argumentos y a su vez utilizar 
los named arguments a la hora de llamar a la función.
'''

#Estructura diccionario:
def saludos (**kwargs): #'kwards' es la convención para los keywords arguments
    print(kwargs)

saludos(first_name = 'Jon', last_name = 'Madariaga') #{'first_name': 'Jon', 'last_name': 'Madariaga'} --> observamos que '**' nos devuelve un diccionario

#Ejemplo básico
def saludo_web(**kwargs):
    if kwargs:
        print(f'Hi {kwargs['first_name']} {kwargs['last_name']}')
    else:
        print('Hi Guest')

saludo_web() #Hi Guest
saludo_web(first_name='Jon', last_name = 'Madariaga') #Hi Jon Madariaga

