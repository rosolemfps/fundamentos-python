def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

texto = input("Digite um texto: ")

print("Quantidade de palavras:", contar_palavras(texto))