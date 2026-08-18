def aluno_aprovado():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    media = (nota_1 + nota_2) / 2

    if media >= 6:
        print("Aluno Aprovado!")
    elif media >= 5 and media < 6:
        print("Aluno de Recuperação!")
    else:
        print("Aluno Reprovado!")

aluno_aprovado()







def login(codigo_secreto=None):
    e_mail = "samuka.rosolem@gmail.com"
    senha = "123456"

    e_mail_input = input("Digite seu e-mail: ")
    senha_input = input("Digite sua senha: ")

    if e_mail_input == e_mail and senha_input == senha:
        print("Usuario Logado!")
        acessar_adimin = input("Deseja acessar area admistartiva?: ")
        if acessar_adimin == "S":
            codigo_secreto_input = input("Digite seu codigo secreto: ")
            if codigo_secreto_input == codigo_secreto:
                print("Acesso Adm Liberado!")
             else:
                print("Código secreto errado!")
        elif acessar_adimin == "N":
            print("Ok. Voce acessou como usuário comum!")
        else:
            print("Opção invalida!")
    else:
        print("E-mail ou senha incorreto!")

login()


login()
