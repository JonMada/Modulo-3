import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts')
print(r.json()) #Nos devuelve la información en formato JSON (ilegible) ¡Tiene estructura de diccionario key - values!
pprint.pprint(r.json()) #Nos devuelve el request en formato más legible

#Si quiero extraer, por ejemplo la primera publicación, funciona como en los diccionarios:
pprint.pprint(r.json()['posts'][0])

#Si de esa primera publicación quiero extraer su url:
pprint.pprint(r.json()['posts'][0]['url_for_post'])