from flask import Flask, render_template, abort
import json

app = Flask(__name__)

# Cargar los datos desde el JSON
with open("data/integrantes.json", encoding="utf-8") as f:
    integrantes = json.load(f)

# Inyectar en todas las plantillas
@app.context_processor
def inject_integrantes():
    return dict(integrantes=integrantes)

@app.route("/")
def index():
    # Pasamos todos los integrantes al index
    return render_template("index.html", integrantes=integrantes)

@app.route("/perfil/<slug>")
def perfil(slug):
    if slug not in integrantes:
        abort(404)
    return render_template("perfil.html", perfil=integrantes[slug])

if __name__ == "__main__":
    app.run(debug=True)
