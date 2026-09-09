def consultar_informacao():
    cliente = {
        "nome": "Carlos",
        "idade": 18,
        "email": "carlos@email.com",
        "cidade": "Piracicaba"
    }

    chave = input("Digite o nome da informação: ")

    valor = cliente.get(chave)

    if valor is not None:
        print("Informação:", valor)
    else:
        print("Informação não encontrada.")


consultar_informacao()