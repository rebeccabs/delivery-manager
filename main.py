import json
# carrega as entregas do arquivo JSON
def carregar_entregas():
    # tenta abrir os arquivos
    try:
        # abre o arquivo em modo leitura
        with open("entregas.json", "r", encoding="utf-8") as arquivo:
            # converte JSON pra lista Python
            return json.load(arquivo)
        # caso o arquivo ainda não exista
    except FileNotFoundError:
        # retorna lista vazia
        return []
    # salva a lista de entregas no arquivo JSON
def salvar_entregas():
    # abre o arquivo em modo escrita
    with open("entregas.json", "w", encoding="utf-8") as arquivo:
        # converte lista Python para JSON
        json.dump(entregas, arquivo, indent=4, ensure_ascii=False)

# lista principal carregada do JSON
entregas = carregar_entregas()
def cadastrar_entrega():
    cliente = input("Nome do cliente: ").strip()
    endereco = input("Endereço de entrega: ").strip()
    if cliente == "" or endereco == "":
        print("Nome e endereço não podem ficar vazios.")
        return
    # estrutura de entrega
    entrega = {
        "cliente": cliente,
        "endereco": endereco,
        "status": "Pendente"
    }
    # aiciona entrega na lsta
    entregas.append(entrega)
    # atualiza arquivo JSON
    salvar_entregas()
    print("Entrega cadastrada com sucesso!")
# exibe todas as entregas cadastradas
def listar_entregas():
    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada.")
    else:
        print("\nEntregas cadastradas:")
        for indice, entrega in enumerate(entregas):
            print(f"{indice + 1}. Cliente: {entrega['cliente']} | Endereço: {entrega['endereco']} | Status: {entrega['status']}")
def atualizar_status():
    if len(entregas) == 0:
        print("Nenhuma entrega para atualizar.")
        return

    for indice, entrega in enumerate(entregas):
        print(f"{indice + 1}. {entrega['cliente']} - {entrega['status']}")

    try:
        numero = int(input("Digite o número da entrega: "))
    except ValueError:
        print("Digite apenas números.")
        return

    if 1 <= numero <= len(entregas):
        entregas[numero - 1]["status"] = "Entregue"
        salvar_entregas()
        print("Status atualizado com sucesso!")
    else:
        print("Número inválido.")

# loop principal do sistema
while True:   
    print("\n=== DELIVERY MANAGER ===")
    print("1 - Cadastrar entrega")
    print("2 - Listar entregas")
    print("3 - Atualizar status")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_entrega()
    elif opcao == "2":
        listar_entregas()
    elif opcao == "3":
        atualizar_status()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")