def votacao():
    idade = int(input("Digite sua idade: "))

    if idade < 16:
        print("Não pode votar")
    elif idade <= 17:
        print("Voto opcional")
    elif idade <= 69:
        print("Voto obrigatório")
    else:
        print("Voto opcional")

votacao()