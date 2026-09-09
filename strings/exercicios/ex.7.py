def procurar_palavra(texto, palavra):
    posicao = texto.find(palavra)

    if posicao == -1:
        print("A palavra não existe no texto.")
    else:
        print("A palavra começa na posição:", posicao)

texto = input("Digite um texto: ")
palavra = input("Digite a palavra que deseja procurar: ")

procurar_palavra(texto, palavra)