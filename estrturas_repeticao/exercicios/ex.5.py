def tabuada(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero = int(input("Digite um número: "))
tabuada(numero)