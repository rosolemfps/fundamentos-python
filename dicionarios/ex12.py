def remover_telefone():
    funcionario = {
        "nome": "Carlos",
        "idade": 30,
        "cargo": "Programador",
        "salario": 3500,
        "telefone": "19999999999"
    }

    print("Antes da remoção:")
    print(funcionario)

    telefone_removido = funcionario.pop("telefone")

    print("\nTelefone removido:", telefone_removido)

    print("\nDepois da remoção:")
    print(funcionario)


remover_telefone()