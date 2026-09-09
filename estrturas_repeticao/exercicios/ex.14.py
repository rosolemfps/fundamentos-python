def calcular_media():
    soma = 0
    quantidade = 0

    while True:
        numero = float(input("Digite um número (0 para parar): "))

        if numero == 0:
            break

        soma += numero
        quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        print("Média:", media)
    else:
        print("Nenhum número foi informado.")


calcular_media()