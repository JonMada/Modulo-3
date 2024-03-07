sentence = 'The quick brown fox jump over the lazy dog'
word = 'quick'

if word in sentence: #Lógica: si mi palabra se encuentra en el string...haz esto
    print('Tu palabra se encuentra en el string')
else:
    print('Tu palabra no se encuentra en el string')

#Un aspecto a tener en cuenta es que hace distinciones entre mayúsculas y minusculas
sentence = 'The quick brown fox jump over the lazy Dog'
word = 'dog'

if word in sentence: 
    print('Tu palabra se encuentra en el string')
else:
    print('Tu palabra no se encuentra en el string')

#Esta situación se resuelve aplicando las minúsculas al contenido de cada variables
    
if word.lower() in sentence.lower(): 
    print('Tu palabra se encuentra en el string')
else:
    print('Tu palabra no se encuentra en el string')


#Trabajando con colecciones de datos:
nums = [1,2,3,4,5,6]

if 4 in nums:
    print('Tú numero se encuentra en la coleccion')
else:
    print('Tú número no se encuentra en la colección')