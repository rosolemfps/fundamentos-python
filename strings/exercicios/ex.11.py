def criar_email(nome, sobrenome, dominio):
    nome = nome.lower()
    sobrenome = sobrenome.lower()

    return nome + "." + sobrenome + "@" + dominio

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
dominio = input("Digite o domínio: ")

print(criar_email(nome, sobrenome, dominio))