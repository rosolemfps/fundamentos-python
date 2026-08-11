def desconto():
 preco = float(input("Digite o preço: "))
 porcentagem = float(input("Digite o desconto em porcentagem: "))

 desconto = preco * porcentagem / 100
 valor_final = preco - desconto

 print("Valor do desconto:", desconto)
 print("Valor final:", valor_final)

desconto()