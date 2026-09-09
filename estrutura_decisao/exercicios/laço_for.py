def somar_numeros():
    total = 0
    for valor in range(1,20):
        total += valor

        print(total)
        somar_numeros()


        def mostrar_numeros_pares():
            for numero in range(1,21):
                if numero % 2 == 0:
                    print(f'numeros pares: {numero}')

        mostrar_numeros_pares()

def mostar_item_da_lista():







    def laco_aninhado():
        nomes = ["rosolem", "amiga larissa","amiga maria", "lz delas"]
        notas = [6,7,8]
        for nome in nomes:
            print(f'nome do aluno: {nome}')
            for nota in notas:
                print(f'nota do aluno: {nota}')

    laco_aninhado()
