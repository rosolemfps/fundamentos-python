def imc():
 peso = float(input("Digite seu peso: "))
 altura = float(input("Digite sua altura: "))

 resultado = peso / (altura * altura)

 print("Seu IMC é:", resultado)

imc()