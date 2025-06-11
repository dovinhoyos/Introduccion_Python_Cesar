from flask import Flask, request, render_template

app = Flask(__name__)

personas = []


@app.route("/")
def inicio():
    return "¡Bienvenido a la aplicación Flask!"


@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"¡Hola, {nombre}!"


@app.route("/tabla")
def showTable():
    return render_template("index.html")


@app.route("/registrarPersona", methods=["GET", "POST"])
def registrarPersona():
    if request.method == "POST":
        nombre = request.form["txtNombres"]
        apellido = request.form["txtApellidos"]
        correo = request.form["txtCorreo"]

        persona = [nombre, apellido, correo]
        personas.append(persona)

        return render_template(
            "tablePersonas.html",
            personas=personas,
            mensaje="Persona Agregada correctamente",
        )
    else:
        return render_template("formPersona.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
