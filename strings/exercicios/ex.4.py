def limpar_texto(texto):
    return texto.strip()

texto = input("Digite um texto com espaços no início e no final: ")

print(limpar_texto(texto))