#Son atributos que se definen directamente dentro de la clase:

class Website:
    title = 'My class title'

#Se puede acceder a él directamente desde la clase:
print(Website.title) #Salida --> 'My class title'

#O desde la instancias (objetos):
web_one = Website()
web_two = Website()

print(web_one.title) #Salida --> 'My class title'
print(web_two.title) #Salida --> 'My class title'
