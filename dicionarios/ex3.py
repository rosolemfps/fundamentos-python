def adicionar_informacoes():
    pessoa = {
        "nome": "Carlos",
        "idade": 18
    }

    pessoa["email"] = input("Digite o email: ")
    pessoa["endereco"] = input("Digite o endereço: ")
    pessoa["telefone"] = input("Digite o telefone: ")

    print("\nInformações cadastradas:")

    for chave, valor in pessoa.items():
        print(chave, ":", valor)


adicionar_informacoes()