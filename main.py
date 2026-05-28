import json
import os 
# nome do arquivo usado pra armazenar entregas
ARQUIVO_ENTREGAS = "entregas.json"

# limpa a tela do terminal de acordo com sistema operacional
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")
# pausa a execução para o usuário ler a mensagem antes de voltar ao menu anterior
def pausar():
    input("\nPressione Enter para continuar...")

# carrega as entregas salvas do arquivo JSON
def carregar_entregas():
    try:
        with open(ARQUIVO_ENTREGAS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
# salva lista atual de entregas no arquivo JSON
def salvar_entregas():
    with open(ARQUIVO_ENTREGAS, "w", encoding="utf-8") as arquivo:
        json.dump(entregas, arquivo, indent=4, ensure_ascii=False)

# lista principal do sistema, carregada ao iniciar o programa
entregas = carregar_entregas()
def cadastrar_entrega():
    limpar_terminal()
    print("=== CADASTRAR ENTREGA ===\n")
    cliente = input("Nome do cliente: ").strip()
    endereco = input("Endereço de entrega: ").strip()
    if cliente == "" or endereco == "":
        print("Nome e endereço não podem ficar vazios.")
        return
    # Cria uma nova entrega com status inicial pendente
    entrega = {
        "cliente": cliente,
        "endereco": endereco,
        "status": "Pendente"
    }
    # Adiciona a nova entrega à lista principal
    entregas.append(entrega)
    # Salva a alteração no arquivo JSON
    salvar_entregas()
    print("Entrega cadastrada com sucesso!")
# exibe todas as entregas cadastradas
def listar_entregas():
    limpar_terminal()
    print("=== LISTA DE ENTREGAS ===\n")
    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada.")
    else:
        print("\nEntregas cadastradas:")
        for indice, entrega in enumerate(entregas):
            print (f"{indice + 1}. CLiente: {entrega['cliente']}")
            print(f"  Endereço: {entrega['endereco']}")
            print(f"  Status: {entrega['status']}")
            print("-" * 30)
def atualizar_status():
    limpar_terminal()
    print("=== ATUALIZAR STATUS ===\n")

    if len(entregas) == 0:
        print("Nenhuma entrega para atualizar.")
    else:
        # Mostra entregas cadastradas
        for indice, entrega in enumerate(entregas):
            print(f"{indice + 1}. CLiente: {entrega['cliente']}")
            print("-" * 30)
        # Valida se o usuário digitou um número
        try:
            numero = int(input("Digite o número da entrega: "))
            # Verifica se a entrega escolhida existe
            if 1 <= numero <= len(entregas):
                entregas[numero - 1]["status"] = "Entregue"
                salvar_entregas()
                print("Status atualizado com sucesso!")
            else:
                print("Número inválido.")
        # Trata entradas inválidas, como letras ou símbolos
        except ValueError:
            print("Digite apenas números.")

def mostrar_menu():
    limpar_terminal()
    print("=== DELIVERY MANAGER ===")
    print("1 - Cadastrar entrega")
    print("2 - Listar entregas")
    print("3 - Atualizar status")
    print("4 - Sair")

# mantém o sistema em execução até o usuário escolher sair
while True:   
    mostrar_menu()

    opcao = input("Escolha uma opção: ")
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
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        pausar()