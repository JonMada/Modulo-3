# '_ _ init _ _'

'''
Es un método especial que se utiliza para inicializar objetos
cuando se crea una instancia de clase. Es el que da los atributos
del objeto.
'''

class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad



persona1 = Persona('Juan', 30)

'''
El método __init__ pasa los valores introducidos en la instancia a los atributos
nombre y edad. Por lo que persona1 ahora tiene un nombre = 'Juan' y una edad = 30.
'''

print(persona1.nombre)
print(persona1.edad)


#Ejemplo desarrollado

class Factura:
    def __init__(self,empresa,deuda):
        self.empresa = empresa
        self.deuda = deuda
    
    def ticket(self):
        return f'{self.empresa} debe un total de: {self.deuda}€'


#Hacemos la instancia para la clase
google = Factura('Google', 1000)
facebook = Factura('Facebook', 2000)

print(google.ticket())
print(facebook.ticket())