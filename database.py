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