def comissao():
 salario = float(input("Digite o salário fixo: "))
 vendas = float(input("Digite o valor das vendas: "))
 porcentagem = float(input("Digite a porcentagem da comissão: "))

 comissao = vendas * porcentagem / 100
 salario_final = salario + comissao

 print("Comissão:", comissao)
 print("Salário final:", salario_final)

comissao()