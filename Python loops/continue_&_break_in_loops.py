#Continue
'''
Lo que hace el siguiente bucle es imprimir los números del 1 al 9,
y cuando el 'num' sea igual a 4, se omite el 'print(num)', prosiguiendo
con el siguiente bucle
'''
for num in range (1,10):
    if num == 4:
        continue
    print(num)

#Break
'''
Lo que hace el siguiente bucle es imprimir los números del 1 al 9,
y cuando el 'num' sea igual a 6, se paraliza el bucle.
'''
for num in range (1,10):
    if num == 6:
        break
    print(num)

#Continue: Ejemplo 2
usernames = ['Jon', 'Valeria', 'Patxi', 'Miren', 'Kel']

for username in usernames:
    if username == 'Miren':
        print(f'Disculpa {username}, no tienes el acceso permitido')
        continue
    else:
        print(f'{username} tienes el acceso permitido')

#Break: Ejemplo 2
usernames = ['Jon', 'Valeria', 'Patxi', 'Miren', 'Kel']

for username in usernames:
    if username == 'Patxi':
        print(f'{username} ha sido encontrado en índice {usernames.index(username)} de la lista')
        break
    print(username)