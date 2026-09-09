def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = valor // nota

        if quantidade > 0:
            print(quantidade, "nota(s) de R$", nota)

        valor = valor % nota

    if valor > 0:
        print("Valor restante:", valor)


caixa_eletronico(187)