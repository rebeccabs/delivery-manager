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
            status TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_entregas_db(cliente, endereco, status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO entregas(cliente, endereco, status)
        VALUES (?, ?, ?)
    """, (cliente, endereco, status))

    conexao.commit()
    conexao.close()


def listar_entregas_db():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, cliente, endereco, status
        FROM entregas
    """)

    entregas = cursor.fetchall()

    conexao.close()

    return entregas


def pesquisar_entregas_db(termo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, cliente, endereco, status
        FROM entregas
        WHERE cliente LIKE ?
    """, (f"%{termo}%",))

    entregas = cursor.fetchall()

    conexao.close()

    return entregas


def buscar_entrega_por_id_db(id_entrega):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, cliente, endereco, status
        FROM entregas
        WHERE id = ?
    """, (id_entrega,))

    entrega = cursor.fetchone()

    conexao.close()

    return entrega


def atualizar_status_db(id_entrega, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE entregas
        SET status = ?
        WHERE id = ?
    """, (novo_status, id_entrega))

    conexao.commit()
    conexao.close()

def excluir_entrega_db(id_entrega):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
        DELETE FROM entregas
        WHERE id = ?
    """, (id_entrega,))

    conexao.commit()
    conexao.close()

def contar_entregas_por_status_db():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM entregas
        GROUP BY status
    """)

    resultados = cursor.fetchall()

    conexao.close()

    return resultados