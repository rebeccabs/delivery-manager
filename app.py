from flask import Flask, render_template, request, redirect

from database import (
    listar_entregas_db,
    cadastrar_entregas_db,
    atualizar_status_db,
    excluir_entrega_db,
    contar_entregas_por_status_db,
    contar_total_entregas_db
)

app = Flask(__name__)

@app.route("/")
def home():

    total = contar_total_entregas_db()

    pendentes = 0
    em_rota = 0
    entregues = 0

    resultados = contar_entregas_por_status_db()

    for resultado in resultados:
        status = resultado[0]
        quantidade = resultado[1]

        if status == "Pendente":
            pendentes = quantidade

        elif status == "Em rota":
            em_rota = quantidade

        elif status == "Entregue":
            entregues = quantidade

    return render_template(
        "index.html",
        total=total,
        pendentes=pendentes,
        em_rota=em_rota,
        entregues=entregues
    )

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

@app.route("/excluir/<int:id_entrega>", methods=["POST"])
def excluir_entrega_web(id_entrega):
    excluir_entrega_db(id_entrega)

    return redirect("/entregas")

app.run(debug=True)