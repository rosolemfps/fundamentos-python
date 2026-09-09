def verificar_chave():
    usuario = {
        "nome": "Carlos",
        "idade": 18,
        "email": "carlos@email.com",
        "cidade": "Piracicaba"
    }

    chave = input("Digite o nome da chave: ")

    if chave in usuario:
        print("A chave existe no dicionário.")
    else:
        print("A chave não existe no dicionário.")


verificar_chave()