def login():
    usuario = {
        "login": "admin",
        "senha": "1234"
    }

    login_digitado = input("Digite o login: ")
    senha_digitada = input("Digite a senha: ")

    if login_digitado == usuario["login"] and senha_digitada == usuario["senha"]:
        print("Login realizado com sucesso!")
    else:
        print("Login ou senha incorretos.")


login()