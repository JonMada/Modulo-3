'''
Lo que buscamos es crear una función a la que le podamos pasar dos argumentos:
1) El texto
2) El tipo de heading (h1,h2,h3...)

Por ejemplo:
heading_generator (title, heading_type)
heading_generator ('Hola', 2) --> <h1>Hola</h1>
'''

#Solución
def heading_generator (title, heading_type):
    return f"<h{heading_type}>{title}</h{heading_type}>"

#Ejemplo de uso
print(heading_generator('Mi primer heading generator',2)) #<h2>Mi primer heading generator</h2>
print(heading_generator('Mi segundo heading generator',1)) #<h1>Mi segundo heading generator</h1>
