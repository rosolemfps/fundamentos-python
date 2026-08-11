def prestacao():
 valor = float(input("Digite o valor do produto: "))
 parcelas = int(input("Digite a quantidade de parcelas: "))

 resultado = valor / parcelas

 print("Valor de cada parcela:", resultado)

prestacao()