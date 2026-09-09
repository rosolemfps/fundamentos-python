def cadastrar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n===== PRODUTOS =====")

        for produto in produtos:
            print("Nome:", produto["nome"])
            print("Preço: R$", format(produto["preco"], ".2f"))
            print("Estoque:", produto["estoque"])
            print("--------------------")


def buscar_produto(produtos):
    nome = input("Digite o nome do produto: ")

    encontrado = False

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("\nProduto encontrado!")
            print("Nome:", produto["nome"])
            print("Preço: R$", format(produto["preco"], ".2f"))
            print("Estoque:", produto["estoque"])
            encontrado = True

    if not encontrado:
        print("Produto não encontrado.")


def atualizar_estoque(produtos):
    nome = input("Digite o nome do produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():

            quantidade = int(input("Digite a quantidade: "))

            tipo = input("Digite A para aumentar ou D para diminuir: ")

            if tipo.upper() == "A":
                produto["estoque"] += quantidade
                print("Estoque aumentado com sucesso!")

            elif tipo.upper() == "D":
                if quantidade <= produto["estoque"]:
                    produto["estoque"] -= quantidade
                    print("Estoque diminuído com sucesso!")
                else:
                    print("Não é possível deixar o estoque negativo.")

            else:
                print("Opção inválida.")

            return

    print("Produto não encontrado.")


def remover_produto(produtos):
    nome = input("Digite o nome do produto que deseja remover: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return

    print("Produto não encontrado.")


def sistema():
    produtos = []

    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar estoque")
        print("5 - Remover produto")
        print("6 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)

        elif opcao == "2":
            listar_produtos(produtos)

        elif opcao == "3":
            buscar_produto(produtos)

        elif opcao == "4":
            atualizar_estoque(produtos)

        elif opcao == "5":
            remover_produto(produtos)

        elif opcao == "6":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


sistema()