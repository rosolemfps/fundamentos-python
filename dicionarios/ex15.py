def cadastro_filme():
    filme = {
        "titulo": "Vingadores",
        "ano": 2012,
        "genero": "Ação",
        "notas": []
    }

    for i in range(5):
        nota = float(input("Digite a nota do filme: "))
        filme["notas"].append(nota)

    media = sum(filme["notas"]) / len(filme["notas"])

    print("\nFilme:", filme["titulo"])
    print("Ano:", filme["ano"])
    print("Gênero:", filme["genero"])
    print("Notas:", filme["notas"])
    print("Média:", media)


cadastro_filme()