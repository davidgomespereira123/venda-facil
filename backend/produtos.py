produtos = []


def cadastrar_produto(nome, preco, estoque):
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"Produto: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Estoque: {produto['estoque']}"
        )
