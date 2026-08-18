def caixa_eletronico():
    saldo = float(input("Digite o saldo disponível: R$ "))
    saque = float(input("Digite o valor que deseja sacar: R$ "))

    if saque > saldo:
        print("Saldo insuficiente")
    elif saque <= 0:
        print("Valor de saque inválido")
    else:
        novo_saldo = saldo - saque
        print("Saque realizado com sucesso")
        print(f"Novo saldo: R$ {novo_saldo:.2f}")


caixa_eletronico()