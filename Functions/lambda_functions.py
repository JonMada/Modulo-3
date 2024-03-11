#Estructura básica  de una función lambda
suma = lambda x,y: x+y

resultado_suma = suma(19,2)
print(resultado_suma) #21

#Ejemplo aplicado:
full_name = lambda first,last: f'{first} {last}' # Creamos nuestra lambda

def saludo(name): #Creamos nuestra función para saludar
    print(f'Buenos días {name}')

saludo(full_name('Jon','Madariaga')) #Aplicamos nuestra lambda a modo de variable, como argumento