def troca():
 a = int(input("Digite o valor de A: "))
 b = int(input("Digite o valor de B: "))

 print("Antes:")
 print("A =", a)
 print("B =", b)

 aux = a
 a = b
 b = aux

 print("Depois:")
 print("A =", a)
 print("B =", b)

troca()