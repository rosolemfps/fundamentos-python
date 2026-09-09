def maior_numero():
    maior = None

    while True:
        numero = float(input("Digite um número: "))

        if maior is None or numero > maior:
            maior = numero

        continuar = input("Deseja continuar? (s/n): ")

        if continuar.lower() == "n":
            break

    return maior


print("Maior número:", maior_numero())