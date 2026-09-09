def validar_telefone(numeros):
    if numeros.isdigit():
        print("Número de telefone válido!")
    else:
        print("Número inválido! Digite somente números.")

telefone = input("Digite o número de telefone: ")

validar_telefone(telefone)