'''
La herencia es un concepto fundamental en la programación orientada
a objetados, ya que permite a una clase (hija/subclase) heredar atributos
y métodos de otra clase (padre/superclase).
'''

#Ejemplo básico 

class Animal: #Superclase
    def __init__(self, nombre):
        self.nombre = nombre
    
class Perro (Animal): #Subclase
    def hacer_sonido(self):
        return 'Guau'

#Creamos objeto

perro = Perro('Bruce')

print(perro.nombre) #Hereda el atributo nombre de la clase animal --> Salida: Bruce
print(perro.hacer_sonido()) #Aplica el método propio de la clase Perro --> Salida: Guau


#Ejemplo 2:

class User: #Clase Padre
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self. last_name = last_name

    def saludo(self):
        return f'Hola {self.first_name} {self.last_name}'
    
class AdminUser (User): #Clase hija
    def usuarios_activos(self):
        return 500

#Instancias:
jon = User('jon@gmail.com', 'Jon', 'Madariaga')
valeria = AdminUser('valeria@gmail.com', 'Valeria', 'Vallejo')

#Aplicación de métodos

# print(jon.usuarios_activos()) #No me deja aplicar este método al objeto ya que percetene a la clase 'User'
print(valeria.saludo()) #Me deja aplicar el método porque pertecene a una subclase del padre, por lo que puede acceder a todos los atributos y métodos
print(valeria.usuarios_activos()) #Me deja aplicar el método porque pertece a la subclase

