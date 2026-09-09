# Mostrando os nomes
def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["luiz", "renan", "ana", "cleiton"]
mostrar_nomes(lista_de_nomes)


# Adicionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)


adicionar_nome(lista_de_nomes, "isabel")


# Adicionando novo nome em uma posição específica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao}: {nomes}")


adicionar_nome_posicao(lista_de_nomes, "rogerio", 2)


# Juntando listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes} foram inseridos: {nomes}")


novos_nomes = ["francisco", "marcio"]
juntar_nomes(lista_de_nomes, novos_nomes)


# Removendo item pelo valor
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido: {nomes}")


remover_nome_pelo_valor(lista_de_nomes, "luiz")


# Removendo nome pelo índice
def remover_nome_posicao(nomes, posicao):
    nome_removido = nomes.pop(posicao)
    print(f"O nome {nome_removido}, da posição {posicao}, foi removido!")


remover_nome_posicao(lista_de_nomes, 4)


# Descobrindo a posição pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Nome não encontrado!")
    else:
        posicao = nomes.index(nome)
        print(f"A posição do nome {nome} é {posicao}")


encontrar_posicao_pelo_valor(lista_de_nomes, "rogerio")


# Contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"A quantidade de nomes da lista é {quantidade}")


quantidade_de_nomes(lista_de_nomes)


# Ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes, reverse=True)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")


ordenar_nomes(lista_de_nomes)


# Operações matemáticas
# Calculando média
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade

    print(f"A média das notas é {media}")


notas_semestre = [7.8, 6.5, 9, 8.7, 9.5]
calcular_media(notas_semestre)


# Gerenciando notas
def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)

    notas_ordenadas = sorted(notas)
    media = sum(notas) / len(notas)

    return notas_ordenadas, media


notas_ordenadas, media = gerenciar_notas(notas_semestre, 3.5)

print(f"Notas ordenadas: {notas_ordenadas}")
print(f"A média das notas: {media}")


# Lista de listas
def adicionar_produto(produtos, produto):
    produtos.append(produto)
    print(f"Minha lista de produtos: {produtos}")


lista_produtos = [
    ["arroz", 2, 32.00],
    ["feijao", 3, 8.50]
]

novo_produto = ["café", 2, 28.00]

adicionar_produto(lista_produtos, novo_produto)


# Quantidade total de produtos
def quantidade_total_produtos(produtos):
    quantidade = 0

    for produto in produtos:
        print(f"Quantidade do produto {produto[0]}: {produto[1]}")
        quantidade += produto[1]

    return sum (quantidade)


total = quantidade_total_produtos(lista_produtos)

print(f"Quantidade total de produtos: {total}")

def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valores.append(produto[1] * produto[2])
        valores.append(valor)

        return sum(valores)

    preco_total_produtos = valor_total_produtos(lista_produtos)
    print('o valor total dos produtos é {preco_total_produtos}')
