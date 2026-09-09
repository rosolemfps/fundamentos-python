def reajuste_preco():
    produto = {
        "nome": "Teclado",
        "preco": 100
    }

    aumento = float(input("Digite o percentual de aumento: "))

    produto["preco"] += produto["preco"] * aumento / 100

    print("Produto:", produto["nome"])
    print("Novo preço: R$", format(produto["preco"], ".2f"))


reajuste_preco()