#En Python una clase es algo así como una plantilla para crear objetos.

class Factura: #Por convención la primera letra de la clase se pone em mayúscula
    def saludo(self): #La función contenida en una clase siempre contiene el argumento 'self'
        return 'Hi there'
    
#Para llamar a la clase tenemos que crear una instancia. Que sería algo así como crear un objeto real utilizando esa plantilla.

factura_uno = Factura() #Estamos creando el objeto 'factura_uno' a partir de la plantilla (class Factura)
print(factura_uno.saludo()) #Nos devuelve 'Hi there'