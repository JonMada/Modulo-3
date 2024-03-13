#Objetivo: extraer las url de los titulos que contegan algo de Python y que la salida sea el texto en formato titulo
#Libraries --> requests, inflection, beautifulsoup4

#Importamos librerias
import requests
from inflection import titleize
from bs4 import BeautifulSoup

#Conectamos con la web
r = requests.get('https://www.dailysmarty.com/topics/python')
print(r) #Response [200] --> solicitud exitosa

#Obtenemos el código HTML de la web a través de la expresión text
r = r.text
print(r)

#Preparamos el código HTML extraído para poder analizarlo:
'''
Para empezar a trabajar con Beautiful Soup es necesario construir 
un objeto de tipo BeautifulSoup que reciba el contenido a analizar:
soup = BeautifulSoup(contents, features='html.parser')
'''
soup = BeautifulSoup(r, features='html.parser')

#Buscamos dentro de cada link (etiqueta <a>):
python_links = soup.find_all('a')

def title_generator(python_links):
    titles = []  # Se inicializa una lista vacía para almacenar los títulos formateados

    def post_formatter(url):
        if 'posts' in url:  # Verifica si la URL contiene 'posts'
            url = url.split('/')[-1]  # Extrae el último segmento de la URL (el título) dividida por '/'
            url = url.replace('-', ' ')  # Reemplaza los guiones con espacios
            url = titleize(url)  # Formatea el título en caso de que no esté capitalizado correctamente
            titles.append(url)  # Agrega el título formateado a la lista de títulos

    # Itera sobre cada enlace en la lista de enlaces proporcionada
    for link in python_links:
        post_formatter(link.get('href',''))
        '''
        La llamada a get con el segundo argumento opcional '' proporciona una cadena vacía 
        si no se encuentra ningún atributo 'href',
        lo que previene errores en caso de que algún enlace no tenga un atributo 'href'
        '''

    return titles

#Introducimos el valor derivado de la función en una variable 'titles'
titles = title_generator(python_links)
#Imprimimos resultados:
for title in titles:
    print(title)
