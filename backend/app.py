from produtos import cadastrar_produto, listar_produtos


def menu():
    while True:
        print("\n================================")
        print("          VENDA FÁCIL")
        print("================================")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")

            preco = float(
                input("Preço do produto: R$ ").replace(",", ".")
            )

            estoque = int(
                input("Quantidade em estoque: ")
            )

            cadastrar_produto(nome, preco, estoque)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida!")


menu()
