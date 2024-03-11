#Ejemplo básico
def saludo(nombre):
    print('Hola',nombre,'!')


saludo('Juan')

#Ejemplo básico 2
def suma(num1,num2):
    return num1 + num2


print(suma(23,23))

#Ejemplo básico 3
def full_name(first,last):
    print(f'{first} {last}')


full_name('Jon','Madariaga')

#Ejemplo básico 4
def autorización(email, password):
    if email == 'jon@gmail.com' and password == '12345':
        print('Accedo autorizado')
    else:
        print('Acceso denegado')


autorización('vale@gmail.com','12345') #Acceso denegado
autorización('jon@gmail.com','12345') #Acceso autorizado

#Ejemplo básico 5 --> no es necesario que las funciones contengan argumentos
def hundred():
    for num in range(1,101):
        print(num)


hundred()

#Ejemplo básico 6 --> un contador dinámico
def counter(max_value):
    for num in range(1,(max_value + 1)):
        print(num)


counter(200)