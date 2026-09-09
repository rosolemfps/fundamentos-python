def separar_dados():
    dados = "João,40,Desenvolvedor,Piracicaba"

    partes = dados.split(",")

    print("Nome:", partes[0])
    print("Idade:", partes[1])
    print("Profissão:", partes[2])
    print("Cidade:", partes[3])

separar_dados()