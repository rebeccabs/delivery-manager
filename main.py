entregas = []
def cadastrar_entrtega():
    cliente = input("Nome do cliente: ")
    endereco = input("Endereço de entrega: ")

    entrega = {
        "cliente": cliente,
        "endereco": endereco,
        "status": "Pendente"
    }
    entregas.append(entrega)
    print("Entrega cadastrada com sucesso!")
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
    else:
        for indice, entrega in enumerate(entregas):
            print(f"{indice + 1}. {entrega['cliente']} - {entrega['status']}")
        numero = int(input("Digite o número da entrega: "))
        if 1 <= numero <= len(entregas):
            entregas[numero - 1]["status"] = "Entregue"
            print("Status atualizado com sucesso!")
        else:
            print("Número inválido.")
while True:   
    print("\n=== DELIVERY MANAGER ===")
    print("1 - Cadastrar entrega")
    print("2 - Listar entregas")
    print("3 - Atualizar status")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_entrtega()
    elif opcao == "2":
        listar_entregas()
    elif opcao == "3":
        atualizar_status()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")