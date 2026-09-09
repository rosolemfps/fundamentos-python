def limpar_telefone(telefone):
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace(" ", "")
    telefone = telefone.replace("-", "")

    return telefone

telefone = input("Digite o telefone: ")

print(limpar_telefone(telefone))