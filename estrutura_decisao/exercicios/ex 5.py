def classificar_nota():
    nota = float(input("Digite a nota: "))

    if nota <= 4:
        print("Insuficiente")
    elif nota <= 6:
        print("Regular")
    elif nota <= 8:
        print("Bom")
    else:
        print("Excelente")

classificar_nota()