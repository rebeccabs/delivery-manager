from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

from database import (
    listar_entregas_db,
    cadastrar_entregas_db,
    atualizar_status_db,
    excluir_entrega_db,
    contar_entregas_por_status_db,
    contar_total_entregas_db,
    pesquisar_entregas_db,
    criar_tabela_usuarios,
    cadastrar_usuario_db,
    buscar_usuario_por_email_db,
    criar_tabela
)

app = Flask(__name__)
app.secret_key = "delivery-manager-chave-secreta"

criar_tabela_usuarios()
criar_tabela()


def usuario_logado():
    return "usuario_id" in session


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        senha_hash = generate_password_hash(senha)

        try:
            cadastrar_usuario_db(nome, email, senha_hash)
            return redirect("/login")
        except:
            return "Erro: e-mail já cadastrado."

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    erro = None

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = buscar_usuario_por_email_db(email)

        if usuario and check_password_hash(usuario[3], senha):

            session["usuario_id"] = usuario[0]
            session["usuario_nome"] = usuario[1]

            return redirect("/")

        else:
            erro = "E-mail ou senha inválidos."

    return render_template(
        "login.html",
        erro=erro
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/")
def home():
    if not usuario_logado():
        return redirect("/login")
    

    usuario_id = session["usuario_id"]

    total = contar_total_entregas_db(usuario_id)
    pendentes = 0
    em_rota = 0
    entregues = 0

    resultados = contar_entregas_por_status_db(usuario_id)

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
    if not usuario_logado():
        return redirect("/login")

    termo = request.args.get("pesquisa")

    usuario_id = session["usuario_id"]

    if termo:
        entregas = pesquisar_entregas_db(termo, usuario_id)
    else:
        entregas = listar_entregas_db(usuario_id)

    return render_template(
        "entregas.html",
        entregas=entregas,
        termo=termo
    )


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if not usuario_logado():
        return redirect("/login")

    if request.method == "POST":
        cliente = request.form["cliente"]
        endereco = request.form["endereco"]

        usuario_id = session["usuario_id"]

        cadastrar_entregas_db(cliente, endereco, "Pendente", usuario_id)

        return redirect("/entregas")

    return render_template("cadastro.html")


@app.route("/atualizar-status/<int:id_entrega>", methods=["POST"])
def atualizar_status_web(id_entrega):
    if not usuario_logado():
        return redirect("/login")

    novo_status = request.form["status"]

    usuario_id = session["usuario_id"]

    atualizar_status_db(id_entrega, novo_status, usuario_id)

    return redirect("/entregas")


@app.route("/excluir/<int:id_entrega>", methods=["POST"])
def excluir_entrega_web(id_entrega):
    if not usuario_logado():
        return redirect("/login")

    usuario_id = session["usuario_id"]

    excluir_entrega_db(id_entrega, usuario_id)

    return redirect("/entregas")


if __name__ == "__main__":
    app.run(debug=True)