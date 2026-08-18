def ingresso():
    idade = int(input("Digite a idade: "))

    if idade <= 5:
        print("Gratuito")
    elif idade <= 12:
        print("R$ 10,00")
    elif idade <= 59:
        print("R$ 20,00")
    else:
        print("R$ 10,00")

ingresso()