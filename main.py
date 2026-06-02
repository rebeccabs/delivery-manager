import json
import os

from database import(
    criar_tabela,
    cadastrar_entregas_db,
    listar_entregas_db
)

criar_tabela()

ARQUIVO_ENTREGAS = "entregas.json"
STATUS_DISPONIVEL = ["Pendente", "Em rota", "Entregue"]


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione Enter para continuar...")

# Carrega as entregas salvas no JSON ao iniciar o sistema
def carregar_entregas():
    try:
        with open(ARQUIVO_ENTREGAS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Salva o estado atual das entregas no arquivo JSON
def salvar_entregas():
    with open(ARQUIVO_ENTREGAS, "w", encoding="utf-8") as arquivo:
        json.dump(entregas, arquivo, indent=4, ensure_ascii=False)


entregas = carregar_entregas()

# Gera um ID único baseado no maior ID já existente
def gerar_proximo_id():
    if len(entregas) == 0:
        return 1

    maior_id = 0

    for entrega in entregas:
        if "id" in entrega and entrega["id"] > maior_id:
            maior_id = entrega["id"]

    return maior_id + 1

# Adiciona ISs às entregas criadas antes da implementação dos mesmos
def corrigir_ids_antigos():
    proximo_id = 1

    for entrega in entregas:
        if "id" in entrega and entrega["id"] >= proximo_id:
            proximo_id = entrega["id"] + 1

    for entrega in entregas:
        if "id" not in entrega:
            entrega["id"] = proximo_id
            proximo_id += 1

    salvar_entregas()


corrigir_ids_antigos()

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
    for entrega in entregas:
        print(f"[{entrega['id']}] Cliente: {entrega['cliente']}")
        print(f"   Status atual: {entrega['status']}")
        print("-" * 30)

# Mostra todas as entregas cadastradas no sistema
def listar_entregas():
    limpar_terminal()
    print("=== LISTA DE ENTREGAS ===\n")

    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada.")
    else:
        print("Entregas cadastradas:\n")
        exibir_entregas()

# Atualiza o status de uma entrega a partir do ID informado
def atualizar_status():
    limpar_terminal()
    print("=== ATUALIZAR STATUS ===\n")

    if len(entregas) == 0:
        print("Nenhuma entrega para atualizar.")
        return

    exibir_entregas_para_atualizacao()

    try:
        id_entrega = int(input("Digite o ID da entrega: "))
        entrega_encontrada = None
# Procura a entrega correspondente ao ID informado
        for entrega in entregas:
            if entrega["id"] == id_entrega:
                entrega_encontrada = entrega
                break

        if entrega_encontrada is not None:
            print("\nEscolha um novo status:")

            for indice, status in enumerate(STATUS_DISPONIVEL):
                print(f"{indice + 1} - {status}")

            opcao_status = int(input("Digite o número do novo status: "))

            if 1 <= opcao_status <= len(STATUS_DISPONIVEL):
                status_atual = entrega_encontrada["status"]
                novo_status = STATUS_DISPONIVEL[opcao_status - 1]

                if status_atual == novo_status:
                    print("A entrega já possui esse status.")
                else:
                    entrega_encontrada["status"] = novo_status
                    salvar_entregas()
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
    print("=== PESQUISAR ENTREGA===\n")

    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada.")
        return

    termo = input("Digite o nome do cliente: ").strip().lower()

    if termo == "":
        print("O campo de pesquisa não pode ficar vazio.")
        return

    encontradas = []

    for entrega in entregas:
        if termo in entrega["cliente"].lower():
            encontradas.append(entrega)

    if len(encontradas) == 0:
        print("Nenhuma entrega encontrada.")
        return

    print("\nEntregas encontradas:\n")
    for entrega in encontradas:
        print(f"[{entrega['id']}] Cliente: {entrega['cliente']}")
        print(f"   Endereço: {entrega['endereco']}")
        print(f"   Status: {entrega['status']}")
        print("-" * 30)

# Remove uma entrega pelo ID
def excluir_entrega():
    limpar_terminal()
    print("=== EXCLUIR ENTREGA ===\n")

    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada.")
        return

    exibir_entregas()

    try:
        id_entrega = int(input("\nDigite o ID da entrega: "))
        for entrega in entregas:
            if entrega["id"] == id_entrega:
                entregas.remove(entrega)
                salvar_entregas()
                print("Entrega excluída com sucesso!")
                return

        print("ID não encontrado.")

    except ValueError:
        print("Digite apenas números.")

def mostrar_estatisticas():
    limpar_terminal()
    print("=== ESTATÍSTICAS ===\n")

    total = len(entregas)
    pendentes = 0
    em_rota = 0
    entregues = 0

    for entrega in entregas:
        if entrega["status"] == "pendente":
            pendentes += 1
        elif entrega["status"] == "Em rota":
            em_rota += 1
        elif entrega["status"] == "Entregue":
            entregues += 1

    print(f"Ttotal de entregues: {total}")
    print(f"Pendentes): {pendentes}")
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