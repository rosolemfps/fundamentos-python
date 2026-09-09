def separar_nome(nome_completo):
    partes = nome_completo.split()

    for parte in partes:
        print(parte)

nome = input("Digite seu nome completo: ")

separar_nome(nome)