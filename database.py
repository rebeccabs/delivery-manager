import sqlite3

NOME_BANCO = "delivery_manager.db"


def conectar():
    return sqlite3.connect(NOME_BANCO)


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entregas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            endereco TEXT NOT NULL,
            status TEXT NOT NULL,
            usuario_id INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def criar_tabela_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_usuario_db(nome, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios(nome, email, senha)
        VALUES (?, ?, ?)
    """, (nome, email, senha))

    conexao.commit()
    conexao.close()


def buscar_usuario_por_email_db(email):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, senha
        FROM usuarios
        WHERE email = ?
    """, (email,))

    usuario = cursor.fetchone()

    conexao.close()

    return usuario


def cadastrar_entregas_db(cliente, endereco, status, usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO entregas(cliente, endereco, status, usuario_id)
        VALUES (?, ?, ?, ?)
    """, (cliente, endereco, status, usuario_id))

    conexao.commit()
    conexao.close()


def listar_entregas_db(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, cliente, endereco, status
        FROM entregas
        WHERE usuario_id = ?
    """, (usuario_id,))

    entregas = cursor.fetchall()

    conexao.close()

    return entregas


def pesquisar_entregas_db(termo, usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    termo = f"%{termo}%"

    cursor.execute("""
        SELECT id, cliente, endereco, status
        FROM entregas
        WHERE usuario_id = ?
        AND (
            cliente LIKE ?
            OR endereco LIKE ?
            OR status LIKE ?
        )
    """, (usuario_id, termo, termo, termo))

    entregas = cursor.fetchall()

    conexao.close()

    return entregas


def atualizar_status_db(id_entrega, novo_status, usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE entregas
        SET status = ?
        WHERE id = ?
        AND usuario_id = ?
    """, (novo_status, id_entrega, usuario_id))

    conexao.commit()
    conexao.close()


def excluir_entrega_db(id_entrega, usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM entregas
        WHERE id = ?
        AND usuario_id = ?
    """, (id_entrega, usuario_id))

    conexao.commit()
    conexao.close()


def contar_entregas_por_status_db(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM entregas
        WHERE usuario_id = ?
        GROUP BY status
    """, (usuario_id,))

    resultados = cursor.fetchall()

    conexao.close()

    return resultados


def contar_total_entregas_db(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM entregas
        WHERE usuario_id = ?
    """, (usuario_id,))

    total = cursor.fetchone()[0]

    conexao.close()

    return total