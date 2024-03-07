#Estructura básica
x = 5

if x > 5:
    print('x es mayor que 5')
elif x < 5:
    print('x es menor que 5')
elif x == 5:
    print('x es igual a 5')
else:
    print('Esta línea no se ejecutará al cumplirse el condicional anterior')

#Ejemplo
edad = 91

if edad < 18:
    print('No tienes edad suficiente para alquilar un coche')
elif edad > 90:
    print(f'Disculpa, con {edad} excede la edad para poder alquilar un coche')
else:
    print(f'Perfecto! {edad} años le permiten alquilar el coche que quiera')
