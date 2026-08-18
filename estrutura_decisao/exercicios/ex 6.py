def maior_numero():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if numero1 > numero2:
        print("O maior é:", numero1)
    elif numero2 > numero1:
        print("O maior é:", numero2)
    else:
        print("Os números são iguais")

maior_numero()