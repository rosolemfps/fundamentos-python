def cadastro_dinamico():
    dados = {}

    quantidade = int(input("Quantas informações deseja cadastrar? "))

    for i in range(quantidade):
        chave = input("Digite o nome da chave: ")
        valor = input("Digite o valor: ")

        dados[chave] = valor

    print("\nDados cadastrados:")
    print(dados)


cadastro_dinamico()