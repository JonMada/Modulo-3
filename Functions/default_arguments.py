#Ejemplo básico
def saludo(name='invitado'): #Invitado será el valor por defecto si no ponemos nada como argumento de la función
    print(f'Hola {name}')


saludo('Jon') #Salida --> Hola Jon
saludo() #Salida --> Hola invitado


#¡¡¡CUIDADO!!! NO UTILIZAR LISTAS COMO ARGUMENTO POR DEFECTO

def some_function(collection = []):
    collection.append(1)
    return collection

print(some_function()) #Sin un argumento collection al que añadir un 1, por defecto añade 1 a una nueva lista
print(some_function()) # [1,1] --> cada vez que llamemos a la función compartirán la misma lista asignada al argumento por defecto