def verificar_extensao(nome_arquivo):
    if nome_arquivo.endswith(".pdf"):
        print("Arquivo válido.")
    else:
        print("Arquivo inválido.")

arquivo = input("Digite o nome do arquivo: ")

verificar_extensao(arquivo)