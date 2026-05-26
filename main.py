entregas = []

while True:
    print("\n=== DELIVERY MANAGER ===")
    print("1 - Cadastrar entrega")
    print("2 - Listar entregas")
    print("3 - Atualizar status")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente = input("Nome do cliente: ")
        endereco = input("Endereço de entrega: ")
        status = "Pendente"

        entrega = {
            "cliente": cliente,
            "endereco": endereco,
            "status": status
        }

        entregas.append(entrega)
        print("Entrega cadastrada com sucesso!")

    elif opcao == "2":
        if len(entregas) == 0:
            print("Nenhuma entrega cadastrada.")
        else:
            print("\nEntregas cadastradas:")
            for indice, entrega in enumerate(entregas):
                print(f"{indice + 1}. Cliente: {entrega['cliente']} | Endereço: {entrega['endereco']} | Status: {entrega['status']}")

    elif opcao == "3":
        if len(entregas) == 0:
            print("Nenhuma entrega para atualizar.")
        else:
            for indice, entrega in enumerate(entregas):
                print(f"{indice + 1}. {entrega['cliente']} - {entrega['status']}")

            numero = int(input("Digite o número da entrega: "))

            if numero >= 1 and numero <= len(entregas):
                entregas[numero - 1]["status"] = "Entregue"
                print("Status atualizado para Entregue.")
            else:
                print("Número inválido.")
    elif opçao == "4":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")