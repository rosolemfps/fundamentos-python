def controle_estoque():
    produto = {
        "nome": "Mouse",
        "preco": 80,
        "estoque": 10
    }

    quantidade = int(input("Digite a quantidade vendida: "))

    if quantidade <= produto["estoque"]:
        produto["estoque"] -= quantidade
        print("Venda realizada!")
        print("Estoque atual:", produto["estoque"])
    else:
        print("Quantidade maior que o estoque disponível.")


controle_estoque()