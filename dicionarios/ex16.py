def lista_compras():
    compra = {
        "cliente": "Maria",
        "produtos": []
    }

    for i in range(5):
        produto = input("Digite o nome do produto: ")
        compra["produtos"].append(produto)

    print("\nCliente:", compra["cliente"])
    print("Produtos comprados:")

    for produto in compra["produtos"]:
        print("-", produto)


lista_compras()