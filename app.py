from flask import Flask, render_template, request, redirect

from database import (
    listar_entregas_db,
    cadastrar_entregas_db,
    atualizar_status_db
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/entregas")
def entregas():
    entregas = listar_entregas_db()

    return render_template(
        "entregas.html",
        entregas=entregas
    )

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        cliente = request.form["cliente"]
        endereco = request.form["endereco"]

        cadastrar_entregas_db(cliente, endereco, "Pendente")

        return redirect("/entregas")

    return render_template("cadastro.html")

@app.route("/atualizar-status/<int:id_entrega>", methods=["POST"])
def atualizar_status_web(id_entrega):
    novo_status = request.form["status"]

    atualizar_status_db(id_entrega, novo_status)

    return redirect("/entregas")

app.run(debug=True)