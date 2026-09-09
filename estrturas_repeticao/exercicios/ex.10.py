def somar_pares(inicio, fim):
    soma = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            soma += numero

    return soma


print(somar_pares(1, 10))