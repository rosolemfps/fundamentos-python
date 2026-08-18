def desconto():
    valor = float(input("Digite o valor da compra: "))

    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = 10
    else:
        desconto = 15

    valor_final = valor - (valor * desconto / 100)

    print("Desconto:", desconto, "%")
    print("Valor final: R$", valor_final)

desconto()