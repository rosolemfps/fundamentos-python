# Anatomia do dicionario


def exibir_aluno():
    aluno = {
        "nome": "Carlos",
        "idade": 18,
        "curso": "Desenvolvimento de Sistemas"
    }
    print('Nome: ', aluno["nome"])
    print('Idade: ', aluno.get("idade"))
    print('Curso: ', aluno["curso"])
    print('Nota: ', aluno.get('nota'))

#exibir_aluno()

# Atualizando Valores
def atualizar_idade():
    aluno = {
        "nome": "Carlos",
        "idade": 18,
        "curso": "Desenvolvimento de Sistemas"
    }

    print('Idade Antes: ', aluno.get('idade'))
    aluno['idade'] = 20
    print('Idade Depois: ', aluno.get('idade'))

#atualizar_idade()

# Adicionando Novas Informações
def adicionar_informacao():
    aluno = {
        "nome": "Carlos",
        "idade": 18
    }
    print('Aluno Antes: ', aluno)
    aluno['curso'] = "Técnico em Eletro-eletronica"
    aluno['nota'] = 9.3
    print('Aluno Depois: ', aluno)

#adicionar_informacao()

# Verificando se uma chave existe
def verificar_chave():
    aluno = {
        "nome": "Carlos",
        "idade": 18
    }

    if 'nome' in aluno:
        print('O nome está cadastrado!')

    if 'nota' not in aluno:
        print('A nota não está cadastrada!')

#verificar_chave()

# Utilizando Comparações
def verificar_aprovacao():
    aluno = {
        "nome": "Carlos",
        "idade": 18,
        "nota": 8.5,
        "frequencia": 88
    }

    if aluno["nota"] >= 6 and aluno["frequencia"] >= 75:
        print(f'O aluno {aluno["nome"]} foi aprovado!')
    else:
        print(f'O aluno {aluno["nome"]} foi reprovado!')

#verificar_aprovacao()

# Percorrendo as Chaves
def listar_campos():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for chave in produto.keys():
        print(chave)

# listar_campos()

# Percorrendo os Valores
def listar_valores():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for valor in produto.values():
        print(valor)

#listar_valores()

# Percorrendo Chaves e Valores
def exibir_produto():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for chave, valor in produto.items():
        print(f'A chave: "{chave}" possui o valor: "{valor}"')

#exibir_produto()

#Atualizando e Calculando
def atualizar_estoque():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    produto['total'] = produto['quantidade'] * produto['preco_unitario']
    print(produto)

#atualizar_estoque()

# Removendo elementos
def remover_informacao():
    produto = {
        "nome": "Caneta Azul",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    # Apaga da memória do programa
    del produto['nome']

    # Apaga e armazena o item em outra variável
    preco_unitario = produto.pop('preco_unitario')
    print(produto, preco_unitario)

#remover_informacao()

# Lista de dicionarios
def listar_produtos():
    produtos = [
        {"nome": "Teclado", "preco": 299.00, "quantidade": 2},
        {"nome": "Mouse", "preco": 25.00, "quantidade": 3},
        {"nome": "Monitor", "preco": 1200.00, "quantidade": 1}
    ]

    total_geral = 0
    for produto in produtos:
        print(f"O produto {produto["nome"]} custa {produto["preco"]}")
        total_individual = produto["preco"] * produto["quantidade"]
        total_geral += total_individual

    print(f'O total geral é: {total_geral}')

#listar_produtos()

# Inserindo Informações Dinamicamente
def cadastrar_aluno():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade: "))
    aluno["curso"] = input("Qual o curso do aluno: ")
    aluno["email"] = input("Digite o e-mail: ")

    print(f'Dados cadastrados! Novo aluno: {aluno}')

#cadastrar_aluno()

def criar_cadastro():
    dados = {}

    quantidade = int(input("Quantos dados você deseja cadastrar? "))

    for item in range(1, quantidade + 1):
        chave = input("Digite o nome do campo: ")
        valor = input(f"Digite o valor de {chave}: ")

        dados[chave] = valor

    print('Cadastro final: ', dados)

#criar_cadastro()

#Dicionario com listas

aluno = {}

def calcular_media(notas):
    return sum(notas) / len(notas)


def aluno_completo():
    aluno = {
        "nome": "Renan",
        "idade": 17,
        "curso": "Desenvolvimento de Sistemas",
        "notas": [8.5, 6.0, 9.3, 8.7],
        "endereco": {
            "cidade": "Piracicaba",
            "rua": "Das Amoreiras",
            "numero": 1257,
            "telefone": "(19) 98847-3687"
        }
    }
    aluno["media"] = calcular_media(aluno['notas'])
    print(aluno["endereco"]["telefone"])

 # aluno_completo()


 def cadastrar_dados_aluno():
    aluno = {}

    aluno["nome "] = input("digite o nome do aluno:")
    aluno["idade"] = int(input("Digite a idade do aluno:"))
    aluno["notas"] = []

    for item in range(4):
        aluno ["notas"].append(float(input("Digite o nota {nota + 1}:")))

        aluno["endereco"] = {}
        aluno["endereco"]["cidade"] = input("digite a cidade do aluno: ")
        aluno["endereco"]["rua"] = input("Digite a rua do aluno: ")
        aluno["endereco"]["numero"] = input("Digite o numero da casa: ")
        aluno["endereco"]["telefone"] = input("Digite o telefone com ddd: ")

        aluno["media"] = calcular_media(aluno['notas'])
        print("aluno cadastrado", json.dumps(aluno, indent=4))

    cadastrar_dados_aluno()
