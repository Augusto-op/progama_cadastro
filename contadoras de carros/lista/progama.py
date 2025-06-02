contatos = []

while True:
    print("\nAGENDA DE CONTATOS")
    print("1 - Cadastrar contato")
    print("2 - Consultar contatos")
    print("3 - Excluir contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        contatos.append(nome)
        print("Contato cadastrado com sucesso!")

    elif opcao == "2":
        print("\nContatos cadastrados:")
        for i, nome in enumerate(contatos):
            print(f"{i + 1} - {nome}")
    elif opcao == "3":
        print("\nContatos cadastrados:")
        for i, nome in enumerate(contatos):
            print(f"{i + 1} - {nome}")
        num = int(input("Digite o número do contato que deseja excluir: "))
        if 0 < num <= len(contatos):
            excluido = contatos.pop(num - 1)
            print(f"Contato '{excluido}' excluído com sucesso!")
        else:
            print("Número inválido.")

    elif opcao == "4":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
