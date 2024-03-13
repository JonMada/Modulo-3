#Core libraries: están integradas dentro de Python
import math 
print(math.sqrt(4))

#Crear nuestros propios módulos
import mi_modulo
print(mi_modulo.saludar('Jon','Madariaga'))

#Cuando queremos importar únicamente un función de la librería
from mi_modulo import saludar
print(saludar('Valeria','Vallejo'))

#Añadir un alías al módulo --> nos permite tener que escribir menos código al referenciar las funciones
import mi_modulo as h #Aquí añadimos el alias 'h' al módulo 'mi_modulo'
print(h.saludar('Miren','Ortega'))

import math as m
print(m.ceil(9.12))

