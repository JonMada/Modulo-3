players = ['Williams','Galarreta','Sancet','Paredes']

#Bucle 'for' aplicado a la list:
for player in players:
    print(player)

'''
En el primer bucle el valor de la variable de iteración (player) es
Williams, por lo que se imprime Williams; en el segundo, Galarreta... 
y así hasta que se terminen los elementos de la secuencia.
'''

#Si cambiamos el elemento a una tupla, el bucle funcionará de la misma manera
players = ('Williams','Galarreta','Sancet','Paredes')
for player in players:
    print(player)

#Bucle 'for' aplicado a dictionaries:
players = {
    'DEL' : 'Williams',
    'MO' : 'Sancet',
    'MD' : 'Galarreta',
    'DEF' : 'Paredes'
}

for position, player in players.items():
    print('Position:',position)
    print('Player Name:',player)

'''
Del primer item, se asociará a la variable "position" la primera parte
del item y la segunda parte a "player"; todo ello de manera automática
'''

#Si quisiesemos sólo aplicar el for a los values:
for player in players.values():
    print('Player Name:',player)

