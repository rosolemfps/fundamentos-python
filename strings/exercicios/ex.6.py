def contar_letra(frase, letra):
    return frase.count(letra)

frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

print("A letra aparece", contar_letra(frase, letra), "vezes.")