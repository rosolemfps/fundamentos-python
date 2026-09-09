def verificar_palavra(texto, palavra):
    if palavra in texto:
        print("Palavra encontrada!")
    else:
        print("Palavra não encontrada!")

texto = input("Digite um texto: ")
palavra = input("Digite uma palavra: ")

verificar_palavra(texto, palavra)