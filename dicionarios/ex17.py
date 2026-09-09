def cadastrar_alunos():
    alunos = []

    for i in range(5):
        print("\nAluno", i + 1)

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        nota = float(input("Digite a nota: "))

        aluno = {
            "nome": nome,
            "idade": idade,
            "nota": nota
        }

        alunos.append(aluno)

    print("\n===== ALUNOS CADASTRADOS =====")

    for aluno in alunos:
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Nota:", aluno["nota"])
        print("--------------------")


cadastrar_alunos()