def jogo_adivinhacao(numero_secreto):
    while True:
        palpite = int(input("Digite seu palpite: "))

        if palpite == numero_secreto:
            print("Você acertou!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")


jogo_adivinhacao(25)