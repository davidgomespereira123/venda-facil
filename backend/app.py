from produtos import cadastrar_produto, listar_produtos


print("================================")
print("       VENDA FÁCIL")
print("================================")


cadastrar_produto("Arroz 5kg", 25.90, 10)
cadastrar_produto("Feijão 1kg", 8.50, 20)
cadastrar_produto("Refrigerante 2L", 9.99, 15)


print("\nProdutos cadastrados:")
listar_produtos()
