def classificar_numero():
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        classificacao = "positivo"
    elif numero < 0:
        classificacao = "negativo"
    else:
        classificacao = "zero"

    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    print(f"Número: {numero}")
    print(f"Classificação: {classificacao} e {paridade}")


classificar_numero()