class Factura:
    def __init__(self,empresa,deuda):
        self.empresa = empresa
        self.deuda = deuda
    

#Hacemos la instancia para la clase
google = Factura('Google', 1000)
facebook = Factura('Facebook', 2000)

#Getter: en Python no necesitamos construir una función, nos permite acceder directamente a los atributos del objeto
print(google.empresa) #Google
print(google.deuda) #1000

#Setter: al igual que con getter, no necesitamos una función, directamente podemos modificar los atributos
google.empresa = 'Yahoo' #Estamos modificando el atributo 'empresa' del objeto 'google'
print(google.empresa) #Yahoo