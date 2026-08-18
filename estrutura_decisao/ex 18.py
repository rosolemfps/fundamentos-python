def calcular_frete():
    compra = float(input("Digite o valor da compra: R$ "))

    if compra <= 100:
        frete = 20
    elif compra <= 300:
        frete = 10
    else:
        frete = 0

    total = compra + frete

    print(f"Valor da compra: R$ {compra:.2f}")
    print(f"Frete: R$ {frete:.2f}")
    print(f"Valor total: R$ {total:.2f}")


calcular_frete()