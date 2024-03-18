class Factura:
    def __init__(self,empresa,deuda):
        self._empresa = empresa #Convención '_' barra baja para indicar que el atributo está protegido
        self._deuda = deuda
    
    def ticket(self):
        return f'{self.empresa} debe un total de: {self.deuda}€'
    
    @property
    def empresa(self):
        return self._empresa
    
    @empresa.setter
    def empresa(self, empresa):
        self._empresa = empresa
    
    @property
    def deuda(self):
        return self._deuda


#Hacemos la instancia para la clase
google = Factura('Google', 1000)
facebook = Factura('Facebook', 2000)

#Getter --> el @property nos permite acceder a la fución como si estuviesemos accediento al atributo '_empresa'
print(google.empresa)
print(google.deuda) 

#Setter --> el @empresa.setter nos permite modificar el cliente
google.empresa = 'Yahoo'
print(google.empresa)

#Como la hemos protegido con 'self._deuda' y no hemos creado una función @property no nos permite ni acceder ni modificar

# google.deuda = 1000 

#No nos deja modificar el atributo ya que está protegido por '_deuda', al estar encapsulada en la función, que nos sirve de protección.

#Tendriamos que forzarlo, pero sabemos que es un indicativo de protegido por lo que sería una mala práctica.
'''
google._deuda = x
print(google._deuda) --> x
'''