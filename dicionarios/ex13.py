def limpar_cadastro():
    funcionario = {
        "nome": "Carlos",
        "idade": 30,
        "cargo": "Programador",
        "salario": 3500,
        "telefone": "19999999999"
    }

    chave = input("Digite a chave que deseja remover: ")

    if chave in funcionario:
        del funcionario[chave]
        print("Chave removida com sucesso!")
    else:
        print("Chave não encontrada.")

    print("\nDicionário atualizado:")
    print(funcionario)


limpar_cadastro()