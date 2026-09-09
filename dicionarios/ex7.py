def verificar_aprovacao():
    aluno = {
        "nome": "Carlos",
        "media": 7.5,
        "frequencia": 80
    }

    if aluno["media"] >= 6 and aluno["frequencia"] >= 75:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")


verificar_aprovacao()