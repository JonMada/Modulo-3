#Custom iterator class

'''
Imaginemos que queremos crear un programa que nos permita
indicar el jugador que va a tirar el penalti, de una lista de 
jugadores. Puede que la lista de jugadores se termine, pero
la tanda de penaltis continúe. Por lo que tendríamos que ser 
capaces de volver al primer elemento de la lista, y volver a iterar
sobre ella, n veces, hasta que esta se termine.
'''

#En el siguiente ejemplo definiremos ese comportamiento

class Alineacion:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.último_indice_jugadores = (len(self.jugadores) -1) #Si la longitud de self.n es menor que la longitud de self.jugadores -1 (queremos controlar el índice)

    def __iter__(self): #Este método nos permitirá la iteración
        self.n = 0 #Esto nos permitirá controlar en que índice de la lista nos encotramos
        return self
    
    def __next__(self): #Este método nos permitirá llamar al siguiente elemento de la lista
        if self.n < self.último_indice_jugadores:
            self.n += 1 #Incrementamos el índice en cada iteración
            jugador = jugadores[self.n] #Jugador es igual al elemento extraido [índice] de la lista jugadores.
            return jugador
        elif self.n == self.último_indice_jugadores:
            self.n = 0 #Nos permite volver de nuevo al primer jugador de la lista jugadores
            jugador = jugadores[self.n] 
            return jugador
            

jugadores = ['Williams','Guruzeta','Sancet', 'Galarreta','Vivian','Paredes', 'Muniain']

#Creamos la instancia:
athletic_lineup = Alineacion(jugadores)
process = iter(athletic_lineup)

#Queremos llamar tantas veces a '__next__' como sea necesario (duranción de la tanda de penalties). Comprobamos:
print(next(process)) #'process' es la convención para la llamada
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 
print(next(process)) 