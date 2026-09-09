from calculaodra import somar, subtrair, multiplicar,dividir

def executar_calculadora():

    operaçoes = {
        "1":somar,
        "2":subtrair,
        "3":multiplicar,
        "4":dividir

    }

    while True:
        print("===========calculadora===========\n")
        print("******ESCOLHA UMA OPÇÂO:******\n")
        print("1 - somar")
        print("2 - subtrair")
        print("3 - multiplicar")
        print("4 - dividir")
        print("0 - sair")

        opçao = input("escolha uma opção: ")

        if opcao == "0":
            print("----calculadora encerrada!----")
            break
