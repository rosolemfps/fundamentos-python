def alterar_informacoes():
    aluno = {
        "nome": "Carlos",
        "idade": 17,
        "telefone": "19999999999",
        "endereco": "Rua A, 100",
        "cidade": "Piracicaba",
        "nota": 8.5,
        "turma": "2ºA",
        "curso": "Desenvolvimento de Sistemas"
    }

    print("Antes das alterações:")
    print(aluno)

    aluno["idade"] = 18
    aluno["cidade"] = "Campinas"

    print("\nDepois das alterações:")
    print(aluno)


alterar_informacoes()