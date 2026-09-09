def cadastrar_pessoa():
    pessoa = {
        "nome": "Carlos",
        "idade": 18,
        "telefone": "19999999999",
        "endereco": "Rua das Flores, 100",
        "cidade": "Piracicaba"
    }

    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("Telefone:", pessoa["telefone"])
    print("Endereço:", pessoa["endereco"])
    print("Cidade:", pessoa["cidade"])


cadastrar_pessoa()