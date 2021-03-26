from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="")

app.config["MONGO_URI"] = "mongodb+srv://admin:admin@clusterjuan.jazv2.mongodb.net/Libreria?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def home():
    lista = mongo.db.libros.find()
    return render_template("home.html", listalibros=lista)


@app.route("/administrador")
def administrador():
    return render_template("admin.html")


@app.route("/clientes")
def clientes():
    listacli = mongo.db.Clientes.find()
    return render_template("clientes.html", listaClientes=listacli)


@app.route("/agregarLibro", methods=['POST'])
def agregarLibro():
    listaAutores = []

    nombres = request.form.getlist('Nombre[]')
    apellido = request.form.getlist('Apellido[]')
    paises = request.form.getlist('Pais[]')

    for i in range(len(nombres)):
        autor = {"Nombre": nombres[i], "Apellido": apellido[i], "Pais": paises[i]}
        listaAutores.append(autor)

    if request.method == "POST":
        mongo.db.libros.insert_one({
            "Titulo": request.form['Titulo'],
            "Editorial": request.form['Editorial'],
            "Edicion": request.form['Edicion'],
            "Autores": listaAutores,
            "Anio": request.form['Anio'],
            "Precio": request.form['Precio']
        })

    return render_template("admin.html")


@app.route("/agregarCliente", methods=['POST'])
def agregarCliente():

    a_direccion = []

    direccion = {"Calle": request.form["Calle"],
                 "Colonia": request.form["Colonia"],
                 "CP": request.form["CP"]}

    a_direccion.append(direccion)

    if request.method == "POST":
        mongo.db.Clientes.insert_one({
            "Nombre": request.form['Nombre'],
            "Apellidos": request.form['Apellidos'],
            "Direccion": a_direccion,
            "Correo": request.form["Correo"]
        })

    return render_template("admin.html")


@app.route("/avanzada")
def avanzada():
    return render_template("avanzada.html")


@app.route("/buscar", methods=['POST'])
def buscar():
    lista = None

    if request.method == "POST":
        lista = mongo.db.libros.find({
            "$or": [
                {"Titulo": {"$eq": request.form['Titulo']}},
                {"Anio": {"$eq": request.form['Anio']}},
                {"Precio": {"$eq": request.form['Precio']}}
            ]
        })

    return render_template("avanzada.html", listalibros=lista)


app.run(debug=True, port=80)
