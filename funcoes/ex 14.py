def consumo():
 distancia = float(input("Digite a distância percorrida: "))
 combustivel = float(input("Digite a quantidade de combustível: "))

 resultado = distancia / combustivel

 print("Consumo médio:", resultado, "km/L")

consumo()