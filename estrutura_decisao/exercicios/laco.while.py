







def soma_com_while():
        while True:
             num_1 =int(input("digite o primeiro valor: "))
             num_2 =int(input("digite o segundo valor: "))

              if num_1 == 0:
                  print("funçao de soma encerrada!")
                 break


             soma = num_1 + num_2
            print(f"o resultado da soma é {soma}")

soma_com_while()