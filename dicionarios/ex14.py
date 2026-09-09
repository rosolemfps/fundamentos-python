def aluno_notas():
    aluno = {
        "nome": "Carlos",
        "notas": [8.0, 7.5, 9.0]
    }

    notas = aluno["notas"]

    media = sum(notas) / len(notas)

    print("Nome:", aluno["nome"])
    print("Notas:", notas)
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))
    print("Média:", media)


aluno_notas()