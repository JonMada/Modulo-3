#Generadores ('yield')

#Ejemplo básico
def generador_pares (n):
    num = 0
    while num < n:
        yield num *2
        num += 1

generador = generador_pares(10)

#Hacemos loop a través de la secuencia generada por el 'yield'
for numero in generador:
    print(numero)


#Ejemplo avanzado
    
class Alineacion:
    def __init__(self, jugadores):
        self.jugadores = jugadores
    
    def alineacion(self):
        alineacion_max = len(self.jugadores)
        idx = 0

        while True:
            if idx < alineacion_max:
                yield self.jugadores[idx]

            else:
                idx = 0
                yield self.jugadores[idx]

            idx += 1
    
    def __repr__(self):
        return f'Alineación: {self.jugadores}'
    
    def __str__(self):
        return f'Alineación de jugadores: {self.jugadores}'
        



athletic = ['Williams','Guruzeta','Sancet', 'Galarreta','Vivian','Paredes', 'Muniain']


alineacion_completa = Alineacion(athletic)
alineacion_athletic = alineacion_completa.alineacion()

#Utilizamos la función next() para ejecutar el generador yield igual que con el método __next__:
print(next(alineacion_athletic))
print(next(alineacion_athletic))
print(next(alineacion_athletic))
print(next(alineacion_athletic))
print(next(alineacion_athletic))
print(next(alineacion_athletic))
print(next(alineacion_athletic))
print(next(alineacion_athletic))

# Williams
# Guruzeta
# Sancet
# Galarreta
# Vivian
# Paredes
# Muniain
# Williams








