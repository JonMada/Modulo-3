'''
Polimorfismo es un principio de la programación orientada a objetos que permite a objetos 
de diferentes clases ser tratados de manera uniforme si cumplen con una interfaz común. 
En Python, el polimorfismo se puede lograr a través de la sobrescritura de métodos.
'''

class ElementoHTML:
    def __init__(self, contenido):
        self.contenido = contenido

class Encabezado(ElementoHTML):
    def generar_html(self):
        return f"<h1>{self.contenido}</h1>"

class Parrafo(ElementoHTML):
    def generar_html(self):
        return f"<p>{self.contenido}</p>"

class Lista(ElementoHTML):
    def generar_html(self):
        items_html = ''.join(f"<li>{item}</li>" for item in self.contenido)
        return f"<ul>{items_html}</ul>"

# Crear instancias de diferentes elementos HTML
encabezado = Encabezado("Título")
parrafo = Parrafo("Este es un párrafo de ejemplo.")
lista = Lista(["Item 1", "Item 2", "Item 3"])

print(encabezado.generar_html())  # Salida: <h1>Título</h1>
print(parrafo.generar_html())     # Salida: <p>Este es un párrafo de ejemplo.</p>
print(lista.generar_html())       # Salida: <ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>

#Otra forma de imprimir sería:

tags = [
    Encabezado('Esto es un título'),
    Parrafo('Esto es un párrafo'),
    Encabezado('Esto es otro título'),
    Lista(['Elemento1', 'Elemento2', 'Elemento3'])
]

for tag in tags:
    print(tag.generar_html())