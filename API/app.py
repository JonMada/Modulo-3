#Importamos Flask
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Ejecutamos en el terminal --> pipenv flask y flask shell. 
#Después ejecutamos el siguiente código: from app import db / db_create_all()
#Cerramos el flask shell --> exit()


#Creamos la instancia(objeto de flask)
app = Flask(__name__)

#Configuramos nuestra base de datos SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Definimos el modelo de la base de datos
class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content   

#Definimos el esquema de serialización
class GuideSchema(ma.Schema):
    class Meta: 
        fields = ('title', 'content')

guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)



#Endpoint para crear una nueva guía
@app.route('/guide', methods=["POST"])
def add_guide():
    title = request.json['title']
    content = request.json['content']

    new_guide = Guide(title, content)

    db.session.add(new_guide)
    db.session.commit()

    guide = Guide.query.get(new_guide.id)

    return guide_schema.jsonify(guide)


#Enpoint para la obtención de los registros (guides) de la base de datos
@app.route("/guides", methods=["GET"])
def get_guides():
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result)


#Endpoint para la obtención de un solo registro (guide) de la base de datos
@app.route("/guide/<id>", methods=["GET"])
def get_guide(id):
    guide = Guide.query.get(id)
    return guide_schema.jsonify(guide)

#Endpoint para actualizar un registro (guide)
@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    guide = Guide.query.get(id)
    title = request.json['title']
    content = request.json['content']

    guide.title = title
    guide.content = content

    db.session.commit()
    return guide_schema.jsonify(guide)

#Endpoint para eliminar un registro (guide)
@app.route("/guide/<id>", methods=["DELETE"])
def guide_delete(id):
    guide = Guide.query.get(id)
    db.session.delete(guide)
    db.session.commit()

    return "Guide was successfully deleted"


#Ejecución
if __name__ == '__main__':
    app.run(debug=True)

