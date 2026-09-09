def cadastro_notas():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")

    aluno["nota1"] = float(input("Digite a primeira nota: "))
    aluno["nota2"] = float(input("Digite a segunda nota: "))
    aluno["nota3"] = float(input("Digite a terceira nota: "))

    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3

    aluno["media"] = media

    print("\nDados do aluno:")
    print(aluno)


cadastro_notas()