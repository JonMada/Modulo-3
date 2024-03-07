# Estructura básica: buscamos que si un número se encuentra entre 1 - 100 (ambos incluidos) imprima 'Éxito'.
number = 101

if number >= 1 and number <=100:
    print('Éxito')
else:
    print('Fracaso')

# 'and' --> ambas condiciones se cumplen
username = 'Jon'
password = '12345'

if username == 'Jon' and password == '12345':
    print('Acceso permitido')
else:
    print('Acceso denegado')

# 'or' --> al menos una condición se cumple
username = 'Pepe'
email = 'jon@gmail.com'

if username == 'Jon' or email == 'jon@gmail.com':
    print('Introduzca su contraseña')
else:
    print('Usuario no encontrado')

# 'not' --> niega la condición. Devuelve True si la condición es False.
number = 45

if not number == 0:
    print('El valor no es igual a 0')
else:
    print('El valor es igual a 0')

#Condicionales compuestos por más de un operador

#Ejemplo1
'''
Clásica página que permite acceder mediante
nombre de usuario o correo. Para ello tendriamos que tener
el nombre de usuario o correo y la contraseña correcta.
'''
username = 'JonMada'
email = 'jonmada@gmail.com'
password = '12345'

if (username == 'JonMada' or email == 'jonmada@gmail.com') and password == '12345':
    print('Acceso permitido')
else:
    print('Acceso restringido')

#Ejemplo2
logged_in = True
standard_user = True

if logged_in and not standard_user:
    print('Puedes acceder al terminal')
else:
    print('No puede acceder al terminal')

'''
Aquí, logged_in y standard_user son variables booleanas 
que ya están establecidas como True, por lo que no necesitas 
compararlas explícitamente con True en la expresión condicional.

La expresión if logged_in and not standard_user: 
verifica si logged_in es True y standard_user es False
'''