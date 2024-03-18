#Ejemplo básico: '__str__'

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self): #El method '__str__' se aplica directamente cuando aplicamos print() al objeto
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    

#Instancia
persona1 = Persona('Juan', 30)

#Aplicamos print()/ también se puede aplicar print(str(persona1))
print(persona1) #Salida --> Nombre: Juan, Edad: 30


#Ejemplo básico: '__repr__'

class Empresa:
    def __init__(self, nombre, empleados):
        self.nombre = nombre
        self.empleados = empleados
    
    def __str__(self):
        return f'Name: {self.nombre}, Empleados: {self.empleados}'
    
    def __repr__(self): #El method '__str__' es buscado directamente cuando aplicamos print a la instancia
        return f'Nombre: {self.nombre}, Empleados: {self.empleados}'

#Instancia
empresa1 = Empresa('Facebok',10000)

'''
Como tenemos en el ejemplo, la clase contiene dos métodos, representación legible
y representación oficial. Ambos pueden ser llamados como print(), en ese caso
prevalecerá el método __str__
'''

#Aplicamos print()/también se puede aplicar print(repr(empresa1))
print(empresa1) #Prevalece el '__str__()' --> Name: Facebok, Empleados: 10000
print(repr(empresa1)) #Salida --> Nombre: Facebok, Empleados: 10000