def verificar_nota():
    nota = float(input("Digite a nota: "))

    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

verificar_nota()