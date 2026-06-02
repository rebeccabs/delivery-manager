import os

from database import (
    criar_tabela,
    cadastrar_entregas_db,
    listar_entregas_db,
    pesquisar_entregas_db,
    buscar_entrega_por_id_db,
    atualizar_status_db,
    excluir_entrega_db,
    contar_entregas_por_status_db
)
criar_tabela()

STATUS_DISPONIVEL = ["Pendente", "Em rota", "Entregue"]

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione Enter para continuar...")

# Cadastra uma nova entrega com status inicial "Pendente"
def cadastrar_entrega():
    limpar_terminal()
    print("=== CADASTRAR ENTREGA ===\n")

    cliente = input("Nome do cliente: ").strip()
    endereco = input("Endereço de entrega: ").strip()

    if cliente == "" or endereco == "":
        print("Nome e endereço não podem ficar vazios.")
        return
    
    cadastrar_entregas_db(cliente, endereco, "Pendente")
    print("Entrega cadastrada com sucesso!")

# Exibe todas as entregas cadastradas
def exibir_entregas():
    entregas = listar_entregas_db()

    for entrega in entregas:
        print(f"[{entrega[0]}] Cliente: {entrega[1]}")
        print(f"   Endereço: {entrega[2]}")
        print(f"   Status: {entrega[3]}")
        print("-" * 30)

# Exibe uma versão resumida das entregas para atualização de status
def exibir_entregas_para_atualizacao():
    entregas = listar_entregas_db()

    for entrega in entregas:
        print(f"[{entrega[0]}] Cliente: {entrega[1]}")
        print(f"   Status atual: {entrega[3]}")
        print("-" * 30)

# Mostra todas as entregas cadastradas no sistema
def listar_entregas():
    limpar_terminal()
    print("=== LISTA DE ENTREGAS ===\n")

    entregas = listar_entregas_db()

    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada.")
    else:
        print("Entregas cadastradas:\n")
        exibir_entregas()

# Atualiza o status de uma entrega a partir do ID informado
def atualizar_status():
    limpar_terminal()
    print("=== ATUALIZAR STATUS ===\n")

    entregas = listar_entregas_db()

    if len(entregas) == 0:
        print("Nenhuma entrega para atualizar.")
        return

    exibir_entregas_para_atualizacao()

    try:
        id_entrega = int(input("Digite o ID da entrega: "))

        entrega_encontrada = buscar_entrega_por_id_db(id_entrega)

        if entrega_encontrada is not None:
            print("\nEscolha um novo status:")

            for indice, status in enumerate(STATUS_DISPONIVEL):
                print(f"{indice + 1} - {status}")

            opcao_status = int(input("Digite o número do novo status: "))

            if 1 <= opcao_status <= len(STATUS_DISPONIVEL):
                status_atual = entrega_encontrada[3]
                novo_status = STATUS_DISPONIVEL[opcao_status - 1]

                if status_atual == novo_status:
                    print("A entrega já possui esse status.")
                else:
                    atualizar_status_db(id_entrega, novo_status)
                    print("Status atualizado com sucesso!")
            else:
                print("Status inválido.")
        else:
            print("ID não encontrado.")

    except ValueError:
        print("Digite apenas números.")

# Pesquisa entregas pelo nome do cliente
def pesquisar_entrega():
    limpar_terminal()
    print("=== PESQUISAR ENTREGA ===\n")

    termo = input("Digite o nome do cliente: ").strip()

    if termo == "":
        print("O campo de pesquisa não pode ficar vazio.")
        return

    encontradas = pesquisar_entregas_db(termo)

    if len(encontradas) == 0:
        print("Nenhuma entrega encontrada.")
        return

    print("\nEntregas encontradas:\n")

    for entrega in encontradas:
        print(f"[{entrega[0]}] Cliente: {entrega[1]}")
        print(f"   Endereço: {entrega[2]}")
        print(f"   Status: {entrega[3]}")
        print("-" * 30)

# Remove uma entrega pelo ID
def excluir_entrega():
    limpar_terminal()
    print("=== EXCLUIR ENTREGA ===\n")

    entregas = listar_entregas_db()

    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada.")
        return

    exibir_entregas()

    try:
        id_entrega = int(input("\nDigite o ID da entrega: "))

        entrega = buscar_entrega_por_id_db(id_entrega)

        if entrega is not None:
            excluir_entrega_db(id_entrega)
            print("Entrega excluída com sucesso!")
        else:
            print("ID não encontrado.")

    except ValueError:
        print("Digite apenas números.")

def mostrar_estatisticas():
    limpar_terminal()
    print("=== ESTATÍSTICAS ===\n")

    entregas = listar_entregas_db()
    total = len(entregas)

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

    print(f"Total de entregas: {total}")
    print(f"Pendentes: {pendentes}")
    print(f"Em rota: {em_rota}")
    print(f"Entregues: {entregues}")
    
def mostrar_menu():
    limpar_terminal()
    print("=== DELIVERY MANAGER ===")
    print("1 - Cadastrar entrega")
    print("2 - Listar entregas")
    print("3 - Atualizar status")
    print("4 - Pesquisar entrega")
    print("5 - Excluir entrega")
    print("6 - Estatísticas")
    print("7 - Sair")

# Mantém o sistema em execução até o usuário escolher sair
while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_entrega()
        pausar()
    elif opcao == "2":
        listar_entregas()
        pausar()
    elif opcao == "3":
        atualizar_status()
        pausar()
    elif opcao == "4":
        pesquisar_entrega()
        pausar()
    elif opcao == "5":
        excluir_entrega()
        pausar()
    elif opcao == "6":
        mostrar_estatisticas()
        pausar()
    elif opcao == "7":
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida.")
        pausar()